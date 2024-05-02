from moviepy.editor import *


clip1 = VideoFileClip("X-Men.97.S01E01.720p.x264-FENiX.mkv").subclip(5,60)
clip1.audio.write_audiofile("X-Men.97.S01E01.720p.x264-FENiX.mp3")