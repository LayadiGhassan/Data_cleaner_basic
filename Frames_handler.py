import cv2
import yt_dlp
import os

def get_frames_generator(source):
    
    
    if 'youtube.com' in source or 'youtu.be' in source:
        ydl_opts = {'format': 'best[ext=mp4]', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(source, download=False)
            source = info['url']

    
    cap = cv2.VideoCapture(source)
    
    if not cap.isOpened():
        
        frame = cv2.imread(source)
        if frame is not None:
            yield frame
        else:
            print(f"Error: Unable to open source {source}")
        return

    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame

    cap.release()
