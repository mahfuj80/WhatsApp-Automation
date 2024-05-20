import pywhatkit as kit
import time

# List of phone numbers with correct format (country code + number)
phone_numbers = [
    "+8801892152455",
    "+8801306627256",
    "+8801306627257"
]

# The message to send
message = "Hello from Oxy Manager! This is an instant WhatsApp message."

# Loop through each phone number and send the message
for phone_number in phone_numbers:
    try:
        # Send the message instantly
        kit.sendwhatmsg_instantly(phone_number, message)
        print(f"Message sent to {phone_number}")
        
        # Wait for 10 seconds before sending the next message
        time.sleep(1)
    except Exception as e:
        # Handle any errors that occur during the message sending
        print(f"Failed to send message to {phone_number}. Error: {e}")