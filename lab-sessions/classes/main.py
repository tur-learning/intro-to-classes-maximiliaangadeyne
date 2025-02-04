from classes import MusicTrack


track1 = MusicTrack("ch1 5ei te", "thasup", "3:04", 176)
track2 = MusicTrack("MY EYES", "Travis Scott", "4:11", 119)

track1.print_info()
track2.print_info()

track1.change_bpm(130)
print("BPM of ch1 5ei te of thasup has changed been from 176 to 130")
track2.convert_duration_to_seconds()



