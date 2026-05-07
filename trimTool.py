import argparse
import ffmpeg

#Uses ffmpeg to return a video based on the start and end times.
#Takes a video file as command line input (ie. 'vid.mp4', 'vid.mov')




def trim(video, start_time, end_time):
    file_ext = str(video).rsplit(".", 1) #splits at last dot, as it parses from right to left
    (
        ffmpeg
        .input(video, ss=start_time, to=end_time)
        .output(file_ext[0] + '_trim.' + file_ext[1]) #concatenates the orignal name of video with _trim modifier
        .run()
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("start_time")
    parser.add_argument("end_time")
    
    args = parser.parse_args()

    trim(args.video, args.start_time, args.end_time)

if __name__ == "__main__":
    main()



