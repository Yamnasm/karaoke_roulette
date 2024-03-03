import random
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    duration: str

class Roulette:
    def __init__(self):
        self.singers = self.get_singers()
        self.songs = self.get_songs()
    
    def spin(self):
        out_dict = {
            "Singer": random.choice(self.singers),
            "Song": random.choice(self.songs)
        }
        return out_dict

    def get_singers(self):
        singers_list = []
        with open("Singers - Karaoke Roulette.txt", "r") as f:
            for line in f.readlines():
                singers_list.append(line.rstrip("\n"))
        return singers_list

    def get_songs(self):
        raw_song_list = []
        with open("Song List - Karaoke Roulette.txt", "r") as f:
            for line in f.readlines():
                raw_song_list.append(line.rstrip("\n"))

        song_dict = []
        for song in raw_song_list:
            song_line_split = song.split(" - ")
            song_dict.append({
                "Song Name": song_line_split[0],
                "Artist": song_line_split[1],
                "Duration": song_line_split[2],
            })
        return song_dict

def main():
    kara = Roulette()
    [print(kara.spin()) for x in range(9)]

if __name__ == "__main__":
    main()