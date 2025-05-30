# System Access Logger

A Python-based system that captures images from a webcam and logs access times, useful for security monitoring and access tracking.

## Features

- Captures images from webcam when triggered
- Logs access timestamps
- Runs silently in the background
- Automatically organizes captured images and logs

## Prerequisites

- Python 3.x
- OpenCV (`cv2`) library
- Windows OS
- Webcam connected to the system

## Installation

1. Clone this repository
2. Install the required Python package:
```bash
pip install opencv-python
```

## Project Structure

```
├── log_access.py      # Main Python script for camera capture and logging
├── hide_terminal.bat  # Batch script to run the Python script
├── run_hidden.vbs     # VBScript to run the batch file without showing terminal
├── log/              # Directory containing captured images and logs
│   ├── access_log.txt # Log file with timestamps
│   └── *.jpg         # Captured images
```

## Usage

To run the logger automatically on system startup or at specific times, you can use Windows Task Scheduler:

1. Open Task Scheduler (Press Win + R, type `taskschd.msc`, and press Enter)
2. Click "Create Basic Task" in the right panel
3. Name and Description:
   - Name: "A custom name" (Camera Access Logger)
   - Description: "Runs the camera access logging system"
   - Click "Next"
4. Trigger Selection:
   - Choose when you want the task to start:
     - "When the computer starts / When the log on" for automatic startup
     - Click "Next"
5. Action Setup:
   - Select "Start a program"
   - Click "Next"
6. Program Details:
   - Program/script: Browse and select the `run_hidden.vbs` file
   - Start in: Enter the full path to your project folder
   - Click "Next"
7. Review the settings and click "Finish"
8. Additional Settings (Optional):
   - Right-click the created task and select "Properties"
   - In the "General" tab:
     - Select "Run whether user is logged on or not"
     - Check "Run with highest privileges"
   - Click "OK" to save changes

Note: Make sure the account running the task has appropriate permissions to access the webcam and write to the log directory.

## Output

- Images are saved in the `log` directory with timestamp-based filenames (format: `picYYYY-MM-DD_HH-MM-SS.jpg`)
- Access times are logged in `log/access_log.txt`

## .gitignore Configuration

The project includes a `.gitignore` file that:
- Ignores all image files (*.jpg, *.jpeg, *.png) in the log directory
- Ignores log files (*.log) and access_log.txt
- Keeps the log directory structure using .gitkeep

## Note

This system is designed for Windows environments and requires appropriate permissions to:
- Access the webcam
- Write to the specified directory
- Execute scripts

## License

MIT License
