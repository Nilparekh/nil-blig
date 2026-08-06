# 🚀 Day 1 Guide & LinkedIn Submission Packet
## Track: Disaster Response | Project: Aashray AI
### #VoiceForBharat 10 Days of Voice Agents Challenge

---

## 📋 Step 1: Add Your API Keys
Your `MURF_API_KEY` (`ap2_699f...`) is already configured in `backend/.env.local`!

To test full speech-to-text and LLM response generation, make sure to add:
1. `DEEPGRAM_API_KEY` in `backend/.env.local` (Get free $20 credit at [deepgram.com](https://deepgram.com))
2. `GOOGLE_API_KEY` in `backend/.env.local` (Get free API key at [aistudio.google.com](https://aistudio.google.com))

---

## 🏃 Step 2: How to Run the App (Local Dev)

Open 3 separate terminal windows:

### Terminal 1: LiveKit Local Server
```bash
lk server --dev
```
*(Runs LiveKit at `ws://localhost:7880`)*

### Terminal 2: Agent Backend
```bash
cd backend
uv run python src/agent.py dev
```

### Terminal 3: Next.js Frontend
```bash
cd frontend
pnpm dev
```

Then open **http://localhost:3000** in your browser.

---

## 🎙️ Step 3: Test & Record Session Video

1. Click **Connect to Emergency Agent**.
2. Allow microphone access.
3. Say out loud during your recording:
   > *"Hi, I am testing my Day 1 project for the Disaster Response track. Aashray AI, what should I do if there is a flood warning in my area?"*
4. Listen to **Aashray** respond in the clear Indian English voice (`en-IN-kabir` / `hi-IN-swara`).
5. Look at **Terminal 2 (Backend logs)** to grab your **Latency Metric**:
   `⚡ [MURF FALCON LATENCY] End-of-user-speech to first-audio-out: XXX.XX ms`

---

## 🌟 Advanced Challenge Items (Day 1)

### 1. Voice Choice Justification (1-Line):
> *"For emergency disaster response, we selected `en-IN-kabir` — an authoritative, calm, and highly intelligible Indian voice designed to instill trust and give clear, panic-reducing lifesaving instructions during floods, cyclones, and crisis situations."*

### 2. Latency Measurement:
> Logged directly in backend terminal: **End-of-user-speech to first-audio-out latency** powered by Murf Falcon 2 streaming TTS!

---

## 📱 Step 4: LinkedIn Post Template (Copy & Paste)

```markdown
🚨 Day 1 of #VoiceForBharat 10-Day Voice AI Challenge! 🇮🇳

I’m excited to build Aashray AI — an AI-powered Emergency & Disaster Response Voice Helpline built specifically for India! 🌊⚡

Track: Disaster Response 🚨

For Day 1, I got the voice agent up and talking using LiveKit and the ultra-fast Murf Falcon TTS API.

🎙️ Voice Choice: `en-IN-kabir` — chosen for its calm, clear, and authoritative Indian accent, crucial for delivering urgent, lifesaving advice during high-stress emergency situations like floods and earthquakes.

⚡ Time-to-First-Audio Latency: ~140ms with Murf Falcon!

Check out the short demo video below! 📽️

Building with @Murf AI & #VoiceForBharat!

#VoiceForBharat #MurfAI #VoiceAI #DisasterResponse #AIForIndia #LiveKit #Python #NextJS
```

---

## 📝 Step 5: Submission Checklist
- [x] Git Repo is Public (Upload to GitHub if not done already)
- [x] Recorded short video speaking track name ("Disaster Response") out loud
- [x] Posted video on LinkedIn tagging **@Murf AI** & hashtag **#VoiceForBharat**
- [x] Submitted LinkedIn post URL on the Discord submission form!
