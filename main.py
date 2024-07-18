import subprocess
import time
import sys
import pyautogui

def send_imessage_to_contact(contact_name, message):
    # Activate Messages app
    subprocess.run(['open', '-a', 'Messages'])

    time.sleep(2)

    # Click on the search bar (coordinates are based on your screen resolution)
    search_bar_position = (90, 85)
    pyautogui.click(search_bar_position)
    time.sleep(1)

    # Type the contact name in the search bar
    pyautogui.write(contact_name)
    time.sleep(2)

    # Press 'Enter' to select the contact in the search results
    pyautogui.press('enter')
    search_bar_position = (60, 190)  # Adjust these coordinates based on your screen
    pyautogui.click(search_bar_position)
    pyautogui.click(search_bar_position)
    time.sleep(1)

    # Type and send the message
    search_bar_position = (800, 805)  # Adjust these coordinates based on your screen
    pyautogui.click(search_bar_position)
    time.sleep(1)
    pyautogui.write(message)
    pyautogui.press('enter')

    sys.exit()

# Get the contact name and message (comment code below for scheduled sends)
contact_name = input("Enter the contact name: ")
message = input("Enter your message: ")

# For scheduled sends through calendar, uncomment below
# contact_name = "First Last"
# message = "Message to Send"


# Send the iMessage to the contact
send_imessage_to_contact(contact_name, message)