# /usr/bin/python3

import os

def video_start():
    #sudo raspivid -o - -t 0 -rot 180 -w 1280 -h 720 -fps 25 -mm average|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
  # os.system("sudo raspivid -rot 180 -w 1280 -h 720 ")
  os.system("sudo raspivid -o - -t 0  -w 1280 -h 720 -fps 25 -mm average|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264")
    #os.system("gst-launch-1.0 -v v4l2src device=/dev/video0 ! 'video/x-raw, width=1280, height=720, framerate=30/1' ! timeoverlay halignment=right valignment=top ! clockoverlay halignment=left valignment=top time-format='%Y/%m/%d %H:%M:%S' ! queue ! videoconvert ! omxh264enc ! h264parse ! flvmux ! rtmpsink location='rtmp://localhost/live live=1'")
#gst-launch-1.0 -v v4l2src device=/dev/video0 ! 'video/x-raw, width=1280, height=720, framerate=30/1' ! timeoverlay halignment=right valignment=top ! clockoverlay halignment=left valignment=top time-format="%Y/%m/%d %H:%M:%S" ! queue ! videoconvert ! omxh264enc ! h264parse ! flvmux ! rtmpsink location='rtmp://localhost/live live=1'
if __name__ == '__main__':
    video_start()