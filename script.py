from moviepy.editor import AudioFileClip, ImageClip

def mp3PNGMerge(fileSaveName):
    audio_clip = AudioFileClip(input("Path to Audio? ").strip('\"'))
    image_clip = ImageClip(input("Path to Image? ").strip('\"'))
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 30
    video_clip.write_videofile(fileSaveName + '.mp4')

name = input("Name? ")
mp3PNGMerge(name)
