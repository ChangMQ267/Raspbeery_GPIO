# /usr/bin/python3

import os

def video_start():
    #sudo raspivid -o - -t 0 -rot 180 -w 1280 -h 720 -fps 25 -mm average|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264

    os.system("sudo raspivid -o - -t 0 -rot 180 -w 1280 -h 720 -fps 25 -mm average|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264")

if __name__ == '__main__':
    video_start()