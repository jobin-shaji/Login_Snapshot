import datetime
import cv2

# Capture the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
else:
    # Read a frame from the camera
    ret, frame = cap.read()
    if ret:
        # Save the frame as an image file
        image_path = f"X:/Custom/mycustomlog/log/pic{current_time}.jpg"
        cv2.imwrite(image_path, frame)
    else:
        print("Error: Could not read frame")

    # Release the camera
    cap.release()

# Log the access time
with open("X:/Custom/mycustomlog/log/access_log.txt", "a") as log_file:
    log_file.write(f"Accessed on: {current_time}\n")
