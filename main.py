import pywhatkit as kit
import pyautogui
import time

# Read phone numbers from the numbers.txt file
with open('numbers.txt', 'r') as file:
    phone_numbers = [line.strip() for line in file]

# Read the message from sms.txt
with open('sms.txt', 'r') as file:
    message = file.read()

# Path to the image
image_path = "images/message.jpg"  # Replace with your image path

# Loop through each phone number and send the image with the message
for phone_number in phone_numbers:
    try:
        # Send the image with the message
        kit.sendwhats_image(phone_number, image_path, message)
        print('Message Sent to:', phone_number)
        # Adjust this time as necessary
        time.sleep(5)
        # Press Ctrl + W to close the current WhatsApp Web tab
        pyautogui.hotkey('ctrl', 'w')
        print("Window Closed")
    except Exception as e:
        print(f"Failed to send image to {phone_number}. Error: {e}")