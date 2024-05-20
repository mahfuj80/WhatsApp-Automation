# WhatsApp Automation

<img src="images/whatsapp.png" alt="WhatsApp Automation" style="margin-right: 10px;"/>

## Overview

This project enables you to automate sending WhatsApp messages using Python. You can send messages to multiple recipients easily and efficiently, which can be useful for reminders, notifications, marketing, and more.

## Features

- **Send Messages Instantly**: Send WhatsApp messages instantly using Python.
- **Multiple Recipients**: Send messages to multiple recipients.
- **Unlimited Messages**: No limits on the number of messages you can send.
- **Global Reach**: Send messages anywhere in the world.

## Requirements

- Python 3.x
- [pywhatkit](https://pypi.org/project/pywhatkit/) library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/whatsapp-automation.git
   cd whatsapp-automation
   ```

2. Install the required Python package:
   ```bash
   pip install pywhatkit
   ```

## Usage

1. **Prepare Your Phone Numbers**: Ensure all phone numbers include the country code and are formatted correctly (e.g., `+8801892152455` for Bangladesh).

2. **Modify the Script**: Update the list of phone numbers and the message in the script.

   ```python
   import pywhatkit as kit
   import time

   # List of phone numbers (with country codes) to send the message to
   phone_numbers = ["+8801892152455", "+8801306627256", "+8801306627257"]
   message = "Hello from Oxy Manager! This is an instant WhatsApp message."

   # Loop through each phone number and send the message
   for phone_number in phone_numbers:
       try:
           kit.sendwhatmsg_instantly(phone_number, message)
           print(f"Message sent to {phone_number}")
           time.sleep(10)  # Wait for 10 seconds before sending the next message
       except Exception as e:
           print(f"Failed to send message to {phone_number}. Error: {e}")
   ```

3. **Run the Script**: Execute the script in your Python environment.
   ```bash
   python send_whatsapp.py
   ```

## Important Considerations

- **WhatsApp Web Login**: Ensure you are logged into WhatsApp Web on your default browser.
- **Browser Configuration**: Ensure your default browser allows pop-ups and is configured to open WhatsApp Web.
- **Rate Limits**: To avoid being blocked by WhatsApp, avoid sending too many messages too quickly.

## Troubleshooting

- If you encounter errors related to invalid phone numbers, ensure they are formatted correctly with the country code.
- If the script fails to open WhatsApp Web, check your internet connection and browser settings.
- For any other issues, refer to the [pywhatkit documentation](https://github.com/Ankit404butfound/PyWhatKit).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Messaging!
