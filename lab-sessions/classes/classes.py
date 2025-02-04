class MusicTrack:
    def __init__(self, title, artist, duration, bpm):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.bpm = bpm

    def print_info(self):
        print(f"Track: {self.title} by {self.artist}")
        print(f"Duration: {self.duration} seconds")
        print(f"BPM: {self.bpm}")

    def change_bpm(self, new_bpm):
        self.bpm = new_bpm
        print(f"BPM changed to {self.bpm}")

    def convert_duration_to_seconds(self):
        minutes, seconds = map(int, self.duration.split(":"))
        total_seconds = minutes * 60 + seconds
        print(f"The duration in seconds of MY EYES by Travis Scott is: {total_seconds} seconds")