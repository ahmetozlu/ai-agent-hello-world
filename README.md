
# 🤖 AI Agent: YouTube Video Summarizer (Hello World Project)

This is a simple **AI Agent** that takes a YouTube video ID and generates a summary using the transcript and OpenAI's GPT model. It's a great Hello World-style project to showcase how you can combine APIs and AI to build smart assistants.

## 📽️ Features

- Fetches transcript from YouTube videos
- Summarizes content using OpenAI GPT-4o model
- Simple terminal-based usage
- Easy to extend or integrate into web apps

## 🚀 How It Works

1. Extracts transcript from YouTube using `youtube-transcript-api`
2. Sends the transcript to OpenAI Chat API
3. Receives and prints a concise summary

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/yt-summary-agent.git
cd yt-summary-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔑 Setup

You need an OpenAI API key to use this tool.

Set your API key using:

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

Or edit the Python script directly:

```python
client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxx")
```

---

## ▶️ Usage

```bash
python summarize.py dQw4w9WgXcQ
```

Replace `dQw4w9WgXcQ` with your YouTube video ID.

### Example Output

```bash
[INFO] Fetching transcript...
[INFO] Generating summary using OpenAI GPT...
Summary:
"This video explains the key concepts of AI Agents using real-life examples..."
```

---

## 🧠 Why This Project?

This "Hello World AI Agent" project shows your ability to:

- Work with external APIs (YouTube, OpenAI)
- Build command-line AI tools
- Create meaningful results from raw data

It can be a great addition to your portfolio if you're looking for freelance opportunities in the field of AI and automation.

---

## 💼 Work With Me

If you're a company or an individual looking for an AI developer, feel free to reach out!

📧 Email: **ahmetozlu93@gmail.com**

---

## 📄 License

MIT License
