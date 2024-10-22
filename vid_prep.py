import os
import cv2
import time

def extract_frames(video_path, frames_path):
    if not os.path.exists(frames_path):
        os.makedirs(frames_path)

    video_capture = cv2.VideoCapture(video_path)
    
    # Check if the video was opened successfully
    if not video_capture.isOpened():
        print(f"Error opening video file: {video_path}")
        return
    
    frame_count = 0
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        frame_filename = os.path.join(frames_path, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    video_capture.release()
    print(f"Extracted {frame_count} frames from: \n{video_path}")



def save_filenames_to_txt(frames_path, txt_path):
    frame_dir = frames_path.split("/")[-1]
    
    try:
        # Get a list of files in the folder
        filenames = os.listdir(frames_path)
        
        # Open the output file in write mode
        with open(txt_path, 'w') as file:
            # Write each filename to the file
            for filename in filenames:
                file.write(f"{frame_dir}/{filename}\n")  ###
        print(f"File names written to: \n{txt_path}")
    
    except Exception as e:
        print(f"Error: {e}")


##  CHANGE VID PATH
video_path = 'C:/Users/pokzh/Desktop/Lane Detection FYP/Ultra-Fast-Lane-Detection/MYCARRYDATA/test_00.mp4' 
vid_file = (video_path.split("/")[-1]).split(".")[0]

#   FRAMES FOLDER AND .TXT FILE NAME MUST BE THE SAME
frames_path = 'C:/Users/pokzh/Desktop/Lane Detection FYP/Ultra-Fast-Lane-Detection/MYCARRYDATA/' + vid_file + '_frames'
txt_path = 'C:/Users/pokzh/Desktop/Lane Detection FYP/Ultra-Fast-Lane-Detection/MYCARRYDATA/' + vid_file + '.txt'

extract_frames(video_path, frames_path)
save_filenames_to_txt(frames_path, txt_path)


