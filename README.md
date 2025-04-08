# Camera Access Logger

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

There are three ways to run the logger:

1. Direct Python execution:
```bash
python log_access.py
```

2. Using the batch file:
```bash
hide_terminal.bat
```

3. Silent mode using VBScript (recommended):
- Double click on `run_hidden.vbs`
- The script will run in the background without showing any terminal window

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

[Add your chosen license here]