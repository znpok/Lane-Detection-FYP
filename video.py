import cv2

def process_video(input_video_path, output_video_path):
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the codec and create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' is a common codec for MP4 files
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Loop over each frame
    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Draw a square in the middle of the frame
        center_x, center_y = frame_width // 2, frame_height // 2
        cv2.circle(frame, (center_x,center_y), 5, (0,255,0), thickness=-1)
        # Write the frame to the output video
        out.write(frame)

        frame_num += 1
        print(f'Processed frame {frame_num}/{frame_count}')

    # Release the video objects
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video = r'C:\Users\pokzh\Desktop\Lane Detection FYP\Ultra-Fast-Lane-Detection\clips\vid1.mp4'  # Path to your input video
    output_video = r'C:\Users\pokzh\Desktop\Lane Detection FYP\Ultra-Fast-Lane-Detection\clips\vid4.mp4'  # Path to save the output video
    process_video(input_video, output_video)  # You can change the square size
