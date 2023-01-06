import os
from moviepy.editor import *

os.chdir("./tempfiles")


vidClip = VideoFileClip("yt_vid.webm")
print("loaded video")
print(f"fps = {vidClip.fps}")
modClip = vidClip.subclip('5:01', '5:10')
print("Extracted clip")
modClip.write_videofile(filename="control.webm",audio=False)
print("Made control.webm")
modClip.write_videofile(filename="p_med.webm",audio=False,preset="medium")
print("Made preset_medium.webm")
modClip.write_videofile(filename="p_slow.webm",audio=False,preset="slow")
print("Made preset_slow.webm")
'''
modClip.write_gif("default.gif")
print("made default.gif")
print("Useing imageio")
modClip.write_gif(filename="imageio_opt__wu.gif", program="imageio",opt="wu")
print("made opt_wu")
modClip.write_gif(filename="imageio_opt_nq.gif", program="imageio",opt="nq")
print("made opt_nq")
modClip.write_gif(filename="imageio_fps_25.gif", program="imageio",fps=25)
print("made fps_25")
print("useing ffmpeg")
modClip.write_gif(filename="ffmpeg_opt_none.gif", program="ffmpeg")
print("made base ffmpeg")
modClip.write_gif(filename="ffmpeg_fps_25.gif", program="ffmpeg",fps=25)
print("made fps_25")
print("useing ImageMagick")
modClip.write_gif(filename="Magick.gif",program="ImageMagick")
print('Magick gif made')
modClip.write_gif(filename="Magick_optp.gif",program="ImageMagick",opt="optimizeplus")
print('optimizeplus gif made')
modClip.write_gif(filename="Magick_optt.gif",program="ImageMagick",opt="OptimizeTransparency")
print('OptimizeTransparency gif made')
# 22MB
modClip.write_gif(filename="Magick_fps_25.gif", program="ImageMagick",fps=25)
print("made fps_25")
'''