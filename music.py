import time
import os
import threading
from pygame import mixer

# --- Lyrics of the song ---
lyrics = [
    "Sahiba aaye ghar kaahe naa,",
    "Aise toh sataaye naa",
    "Dekhun tujhko chain aata hai,",
    "Sahiba neendein veendein aaye naa",
    "Raatein kaati jaaye naa",
    "Tera hi khayaal din rain aata hai!",
    "Sahiba samandar, meri aankhon mein reh gaye,",
    "Hum aate aate jaana teri yaadon mein reh gaye,",
    "Yeh palke gawahi hai, hum raaton mein reh gaye",
    "",
    "Jo waade kiye saare, bas baaton mein reh gaye",
    "Baaton baaton mein hi, khwaabon khwaabon mein hi, mere qareeb hai tu,",
    "Teri talab mujhko teri talab jaana ho tu kabhi rubaroo,",
    "Shor sharaba jo seene mein hai mere, kaise bayaan main karun?",
    "Haal jo mera hai main kisko bataun? Mere…",
    "Sahiba dil naa kiraaye ka,",
    "Thoda toh sambhaalo naa,",
    "Naazuk hai yeh toot jaata hai",
    "Sahiba neendein veendein aaye naa",
    "Raatein kaati jaaye naa",
    "Tera hi khayaal din rain aata hai!",
    "Kaisi bhala shab hogi woh sang jo tere dhalti hai,",
    "Dil ko koi khwahish nahi, teri kami khalti hai",
    "Aaram naa ab aankhon ko, khwaab bhi naa badalti hai",
    "Dil ko koi khwahish nahi, teri kami jaana khalti hai",
    "Sahiba, tu hi mera aaina,",
    "Haathon mein bhi mere haan,",
    "Tera hi naseeb aata hai,",
    "Sahiba neendein veendein aaye naa",
    "Raatein kaati jaaye naa",
    "Tera hi khayaal din rain aata hai!"
]

# --- Utility functions ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_music(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

def display_lyrics(lyrics, total_duration):
    clear_screen()
    print("Now Playing: Sahiba - Aditya Rikhari\n")

    num_lines = len(lyrics)
    time_per_line = (total_duration / num_lines) * 0.5 # sync each line with song duration

    for line in lyrics:
        print(line)
        time.sleep(time_per_line)

    print("\n-- End of Lyrics --")

# --- Main Execution ---
if __name__ == "__main__":
    # Change this to the path of your local 'Sahiba.mp3'
    song_path = "Sahiba.mp3"

    # Total duration of the song in seconds (3:01)
    total_duration = 181  

    # Run music in a separate thread
    music_thread = threading.Thread(target=play_music, args=(song_path,))
    music_thread.start()

    # Run lyrics display
    display_lyrics(lyrics, total_duration)

    # Wait for music to finish
    music_thread.join()
