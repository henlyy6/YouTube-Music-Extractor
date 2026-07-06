import os
import sys
import re
from yt_dlp import YoutubeDL

def download_youtube_mp3():
    # 1. Ask where to save once at the very start
    download_path = input("📂 Enter the folder path to save the MP3s (or press Enter for current folder): ").strip()
    if not download_path:
        download_path = "."
    
    download_path = os.path.abspath(download_path)
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Automatically looks in the exact same folder as this script file for ffmpeg.exe
    current_script_folder = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Base setup options
    ydl_opts = {
        'default_search': 'ytsearch1', 
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(id)s.%(ext)s'),
        'ffmpeg_location': current_script_folder,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    # 2. Loop forever so you can keep adding songs!
    while True:
        print("\n" + "="*40)
        user_input = input("🎵 Enter song name (or type 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("👋 Goodbye! Happy listening!")
            break
            
        if not user_input:
            print("❌ You didn't enter anything!")
            continue

        search_query = f"{user_input} official audio music lyric track"
        print(f"🔍 Searching YouTube for clean audio...")
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(f"ytsearch1:{search_query}", download=False)
                
                if 'entries' in info_dict and len(info_dict['entries']) > 0:
                    video_info = info_dict['entries'][0]
                    video_title = video_info.get('title', None)
                    video_id = video_info.get('id', None)
                    
                    if video_title and video_id:
                        # 📌 THE NEW HEAVY-DUTY CLEANER
                        # 1. Strip out the annoying keyword phrases entirely
                        clutter_words = r'(?i)\b(official audio|official music video|official video|official|audio|music|lyric|lyrics|track|video|hd|hq|visualizer|feat|ft)\b'
                        cleaned_title = re.sub(clutter_words, '', video_title)
                        
                        # 2. Zap all shapes and sizes of brackets and quotation marks (including sneaky wide ones)
                        cleaned_title = re.sub(r'[\(\)\[\]\{\}＂""“”‘’]', '', cleaned_title)
                        
                        # 3. Clean up messy leftover spacing
                        cleaned_title = re.sub(r'\s+', ' ', cleaned_title).strip()
                        
                        # 4. Remove ugly trailing/leading symbols left behind (dashes, underscores, etc.)
                        cleaned_title = re.sub(r'^[-_\s]+|[-_\s]+$', '', cleaned_title).strip()

                        # Strip illegal Windows filename characters
                        safe_title = "".join([c for c in cleaned_title if c not in r'\/:*?"<>|'])
                        
                        if not safe_title:
                            safe_title = "Downloaded_Song"

                        final_filename = f"{safe_title}.mp3"
                        full_final_path = os.path.join(download_path, final_filename)
                        
                        # Check if this cleaned track already exists
                        if os.path.exists(full_final_path):
                            print(f"🛑 Skipping! '{final_filename}' already exists in this folder.")
                            continue
                        
                        print(f"📥 Found: {safe_title}")
                        print("📥 Downloading and converting now...")
                        
                        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
                        
                        temp_mp3_path = os.path.join(download_path, f"{video_id}.mp3")
                        if os.path.exists(temp_mp3_path):
                            os.rename(temp_mp3_path, full_final_path)
                            
                        print(f"✅ Success! Saved as: {final_filename}")
                else:
                    print("❌ No matches found on YouTube.")
                
        except Exception as e:
            print(f"❌ Oops, something went wrong: {e}")

if __name__ == "__main__":
    download_youtube_mp3()
