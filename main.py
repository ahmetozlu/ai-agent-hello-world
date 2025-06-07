import os
import openai
import re
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv

load_dotenv()
openai.api_key = "YOUR_OPEN_API_KEY"


def extract_video_id(youtube_url_or_id):
    # Extracts the video ID from a full URL or returns the ID if already provided
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, youtube_url_or_id)
    if match:
        return match.group(1)
    return youtube_url_or_id


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t["text"] for t in transcript])
    except Exception as e:
        print(f"[ERROR] Could not retrieve transcript: {e}")
        return None


def summarize_text(text, mode="summary"):
    prompt = ""

    if mode == "summary":
        prompt = f"Please summarize the following video transcript:\n{text}"
    elif mode == "keywords":
        prompt = f"Extract the most important keywords from this transcript:\n{text}"
    elif mode == "title":
        prompt = f"Suggest a short, SEO-friendly title for the following transcript:\n{text}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"[ERROR] OpenAI API failed: {e}")
        return None


def main():
    print("🎥 Smart Video Summarizer\n")
    video_input = input("Enter YouTube video URL or ID: ").strip()
    video_id = extract_video_id(video_input)

    print("\n⏳ Retrieving transcript...")
    transcript = get_transcript(video_id)

    if not transcript:
        print("❌ Transcript not available. Make sure the video has captions.")
        return

    print("\n✍️ Generating summary...")
    summary = summarize_text(transcript, mode="summary")
    print("\n📄 Summary:\n", summary)

    print("\n🔍 Generating keywords...")
    keywords = summarize_text(transcript, mode="keywords")
    print("\n🏷️ Keywords:\n", keywords)

    print("\n📝 Suggesting a title...")
    title = summarize_text(transcript, mode="title")
    print("\n📌 Suggested Title:\n", title)


if __name__ == "__main__":
    main()

