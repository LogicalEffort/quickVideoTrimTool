import sys
import ffmpeg

#Uses ffmpeg to return a video based on the start and end times.
#Takes a video file as command line input (ie. 'vid.mp4', 'vid.mov')
video = sys.argv[1]
start_time = sys.argv[2]
end_time = sys.argv[3]

file_ext = str(video).split(".") #splits file extension for allowance of different formats
(
    ffmpeg
    .input(video, ss=start_time, to=end_time)
    .output(file_ext[0].removesuffix(".") + '_trim.' + file_ext[1]) #concatenates the orignal name of video with _trim modifier
    .run()
)

