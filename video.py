# /usr/bin/python3

import os

def video_start():
    #sudo raspivid -o - -t 0 -rot 180 -w 1280 -h 720 -fps 25 -mm average|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
  # os.system("sudo raspivid -rot 180 -w 1280 -h 720 ")
    os.system("sudo raspivid -o - -t 0  -w 1280 -h 720 -fps 50 -mm average|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264 --h264-fps = 50 &")
    #os.system("raspivid - o - -t 0 -vf -w 800 -h 400 -fps 24|cvlc -v stream:///dev/stdin --sout '#rtp{sdp=rtsp://127.0.0.1:8090/}' :demux=h264")#raspivid - o - -t 0 -vf -w 800 -h 400 -fps 24|cvlc -v stream:///dev/stdin --sout‘rtp{sdp=rtsp://:8090/}‘:demux=h264
    #os.system("gst-launch-1.0 -v v4l2src device=/dev/video0 ! 'video/x-raw, width=1280, height=720, framerate=30/1' ! timeoverlay halignment=right valignment=top ! clockoverlay halignment=left valignment=top time-format='%Y/%m/%d %H:%M:%S' ! queue ! videoconvert ! omxh264enc ! h264parse ! flvmux ! rtmpsink location='rtmp://localhost/live live=1'")
    #os.system(
    #    "gst-launch-1.0 -v v4l2src device=/dev/video0 ! 'video/x-raw, width=1280, height=720, framerate=30/1' ! timeoverlay halignment=right valignment=top ! clockoverlay halignment=left valignment=top time-format='%Y/%m/%d %H:%M:%S' ! queue ! videoconvert ! omxh264enc ! h264parse ! flvmux ! rtmpsink location='rtmp://localhost/fish/live live=1' &")
    #ffmpeg -re -i rtmp://ip:9999/myapp/room1-vcodec libx264 -vprofile baseline -acodec libmp3lame -ar 44100 -ac 1 -f flv rtmp://localhost/live

#gst-launch-1.0 -v v4l2src device=/dev/video0 ! 'video/x-raw, width=1280, height=720, framerate=30/1' ! timeoverlay halignment=right valignment=top ! clockoverlay halignment=left valignment=top time-format="%Y/%m/%d %H:%M:%S" ! queue ! videoconvert ! omxh264enc ! h264parse ! flvmux ! rtmpsink location='rtmp://localhost/live live=1'
if __name__ == '__main__':
    video_start()