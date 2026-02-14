# telepresence_logic.py
# Basic Telepresence Robot Logic
# This script demonstrates camera capture and robot movement logic

# -------------------------------
# Import Libraries
# -------------------------------
import socket
import cv2


# -------------------------------
# Function: Robot Movement Logic
# -------------------------------
def move_robot(command):
    """
    This function simulates robot movement.
    In real robot, GPIO or motor driver signals will be sent here.
    """

    if command == "FORWARD":
        print("Robot moving forward")

    elif command == "LEFT":
        print("Robot turning left")

    elif command == "RIGHT":
        print("Robot turning right")

    elif command == "STOP":
        print("Robot stopped")

    else:
        print("Invalid command")


# -------------------------------
# Function: Camera Capture Logic
# -------------------------------
def get_camera_frame():
    """
    Captures one frame from camera
    and converts it to grayscale.
    """

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not detected")
        return

    ret, frame = cap.read()

    if ret:
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print("Camera working - frame captured")

    else:
        print("Failed to capture frame")

    cap.release()


# -------------------------------
# Main Program Execution
# -------------------------------
if __name__ == "__main__":

    print("System Initialized")

    # Test camera
    get_camera_frame()

    # Test robot command
    move_robot("FORWARD")
