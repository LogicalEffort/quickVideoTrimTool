# FFMPEG Trim Tool

## How to execute:
Place the .exe and the video you want to trim into the same folder and run the following command from that directory:</br>
</br>`./trimTool.exe nameofclip.mp4 00:01:15 00:01:24`</br>
</br>The timestamps must be in HH:MM:SS format, where the first timestamp is the start of the clip and the second is where you want the trimmed video to end. </br>
</br>The video clips can be .mp4, .mov, .mkv, etc (the example was just .mp4).</br>
## Output
A trimmed version of the video (in the original format) will be created in the same directory but with an "_trim" appended to the original title. (i.e. "*nameofclip_trim.mp4*")
