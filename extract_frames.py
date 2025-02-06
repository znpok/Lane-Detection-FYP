import cv2
import os

def extract_frames(video_path, output_folder):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Check if the video was opened successfully
    if not video_capture.isOpened():
        print(f"Error opening video file: {video_path}")
        return
    
    frame_count = 0
    while True:
        # Read a frame from the video
        success, frame = video_capture.read()
        
        # If the frame was not read successfully, we're done
        if not success:
            break
        
        # Save the frame as a JPEG file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        
        # Move to the next frame
        frame_count += 1
    
    # Release the video capture object
    video_capture.release()
    print(f"Extracted {frame_count} frames from {video_path}.")

# Example usage:
video_path = r'C:\Users\pokzh\Desktop\Lane Detection FYP\Ultra-Fast-Lane-Detection\MYCARRYDATA\vid1.mp4'
output_folder = r'C:\Users\pokzh\Desktop\Lane Detection FYP\Ultra-Fast-Lane-Detection\MYCARRYDATA\frames'
extract_frames(video_path, output_folder)
