import logging
import os
import time

from dotenv import load_dotenv
from livekit import rtc
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    JobProcess,
    cli,
    tokenize,
    room_io,
)
from livekit.plugins import murf, silero, openai, deepgram, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("agent")

load_dotenv(".env.local")

# Disaster Response System Prompt (#VoiceForBharat Edition)
SYSTEM_PROMPT = """You are Aashray, India's AI Disaster Emergency and Crisis Response Assistant for the #VoiceForBharat project.
Your primary role is to assist citizens, first responders, and emergency victims during natural disasters such as floods, cyclones, earthquakes, heatwaves, landslides, and urban emergencies across India.

Key instructions:
1. Always speak calmly, clearly, authoritatively, and compassionately in short, actionable sentences.
2. Provide immediate life-safety advice (e.g. move to elevated ground during floods, shut off main gas/electric switches during earthquakes, dial national emergency helpline 112 or NDRF helpline 1070).
3. Keep responses concise, direct, and under 2-3 short sentences so speech output remains fast and natural.
4. Do NOT use markdown symbols, formatting, emojis, bullet points, or special characters. Speak directly as if on a radio broadcast or emergency helpline.
"""


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=SYSTEM_PROMPT)


server = AgentServer()


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


server.setup_fnc = prewarm


@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Use Groq (free, ultra-fast LLM) via OpenAI-compatible API
    groq_llm = openai.LLM(
        model="llama-3.1-8b-instant",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY", ""),
    )

    # Set up voice AI pipeline: Groq LLM + Murf Falcon TTS + Deepgram STT
    session = AgentSession(
        stt=deepgram.STT(model="nova-3"),
        llm=groq_llm,
        tts=murf.TTS(
            voice="en-IN-samar",  # Valid Murf Falcon Indian English Male voice
            tokenizer=tokenize.basic.SentenceTokenizer(min_sentence_len=2),
            text_pacing=True
        ),
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        preemptive_generation=True,
    )

    # Latency tracking (Advanced Task: log end-of-user-speech to first audio out)
    user_speech_end = 0.0

    @session.on("user_speech_committed")
    def _on_user_speech(msg):
        nonlocal user_speech_end
        user_speech_end = time.perf_counter()

    @session.on("agent_speech_started")
    def _on_agent_speech(msg):
        nonlocal user_speech_end
        if user_speech_end > 0:
            latency_ms = (time.perf_counter() - user_speech_end) * 1000
            logger.info(f"⚡ [MURF FALCON LATENCY] End-of-user-speech to first-audio-out: {latency_ms:.2f} ms")

    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=lambda params: (
                    noise_cancellation.BVCTelephony()
                    if params.participant.kind
                    == rtc.ParticipantKind.PARTICIPANT_KIND_SIP
                    else noise_cancellation.BVC()
                ),
            ),
        ),
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(server)
