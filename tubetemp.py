from pytube import YouTube

clip_link = "https://youtu.be/H4e7QOTXUo4"
#"https://youtu.be/H4e7QOTXUo4"
#"https://www.youtube.com/watch?v=cgM5qaU5Bjw"

video_url = str(clip_link)

videoobj = YouTube(url=video_url)

video_streams = videoobj.streams

''' GOAL
[res, audio] = itag
res, audio?

all need to be webm or progressive
'''

resaudio_itag = {}

with open("temp_log.txt", "wt") as log:
    
    # print all streams line by line
    s = str(video_streams).split(',')
    for x in s:
        log.write(f'{x} \n')
    
    # print all available resolutions
    log.write("All available resolutions \n")
    for x in video_streams:
        log.write(f" {x.resolution}, Has Audio: {x.includes_audio_track}, Progressive?: {x.is_progressive} \n")
    
    webm_streams = video_streams.filter(file_extension="webm", type="video")
    log.write("\n Only showing webm with video streams \n")
    for x in webm_streams:
        print(type(x))
        log.write(f"{x} \n")
        t = f"{x.resolution} audio: {x.is_progressive}"
        resaudio_itag[t] = x.itag
    print(resaudio_itag)
    
    pro_streams = video_streams.filter(progressive=True)
    log.write("Only showing progressive streams \n")
    for x in pro_streams:
        log.write(f"{x} \n")
        t = f"{x.resolution} audio: {x.is_progressive}"
        resaudio_itag[t] = x.itag
        
    adp_streams = video_streams.filter(progressive=False)
    log.write("Only showing adaptive streams \n")
    for x in adp_streams:
        log.write(f"{x} \n")
        
    # goal?
    
    log.write("goal? \n")
    for x in resaudio_itag:
        log.write(f"{x}, itag: {resaudio_itag[x]} \n")
    
    
    
    
    
    
    
    
    

