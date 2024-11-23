import cv2
import numpy as np
import pyautogui

def start_screen_recording(output_path="screen_recording.avi", fps=30):
    
    screen_size = pyautogui.size()  # Get screen size
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"XVID"), fps, screen_size)

    print("Screen recording started. Press 'q' to stop.")
    try:
        while True:
            frame = np.array(pyautogui.screenshot())  # Capture screen
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert for OpenCV
            out.write(frame)  # Write frame to video
            cv2.imshow("Recording", frame)  # Show live recording

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop if 'q' is pressed
                print("Screen recording stopped.")
                break
    finally:
        out.release()  # Release resources
        cv2.destroyAllWindows()
