import pywhatkit as kit
import time

# List of phone numbers with correct format (country code + number)
# Read phone numbers from the numbers.txt file
with open('numbers.txt', 'r') as file:
    phone_numbers = [line.strip() for line in file]


# The message to send
message = "Hello from Oxy Manager! This is an instant WhatsApp message."

# Loop through each phone number and send the message
for phone_number in phone_numbers:
    try:
        kit.sendwhatmsg_instantly(phone_number, message)
        print(f"Message sent to {phone_number}")
        time.sleep(10)  # Wait for 10 seconds before sending the next message
    except Exception as e:
        print(f"Failed to send message to {phone_number}. Error: {e}")