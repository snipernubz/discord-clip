from moviepy.editor import *


vidClip = VideoFileClip("yt_vid.webm")
print("loaded video")
modClip = vidClip.subclip(301, 310)
print("Extracted clip")
modClip.write_gif("result_n.gif")
print("made norm.gif")
modClip.write_gif(filename="result_wu.gif", program="imageio",opt="wu")
print("made result_wu")
modClip.write_gif(filename="result_nq.gif", program="imageio",opt="nq")
print("made result_nq")
modClip.write_gif(filename="result_optp.gif",program="ImageMagick",opt='optimizeplus')
print('optimizeplus gif made')
modClip.write_gif(filename="result_optt.gif",program="ImageMagick",opt='OptimizeTransparency')
print('OptimizeTransparency gif made')
