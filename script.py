from moviepy.editor import AudioFileClip, ImageClip
print("Don't set FPS to 1 otherwise audio won't work")

def mp3PNGMerge(fileSaveName):
    audio_clip = AudioFileClip(input("Path to Audio? ").strip('\"'))
    image_clip = ImageClip(input("Path to Image? ").strip('\"'))
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    fp = int(Input("Frames per second? (Integer only)"))
    video_clip.fps = fp
    video_clip.write_videofile(fileSaveName + '.mp4')

name = input("Name? ")
mp3PNGMerge(name)
