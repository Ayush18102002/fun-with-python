from moviepy import VideoFileClip

clip = VideoFileClip("video.mp4")

clip.write_gif("output.gif")

print("gif saved successfully as output.gif")

