import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("Step 1: Opening Chrome browser...")
time.sleep(2)

# Open Windows Run
pyautogui.hotkey("win", "r")
time.sleep(2)

# Search for Chrome
pyautogui.write("chrome", interval=0.1)
pyautogui.press("enter")

time.sleep(1)

print("Chrome launch command completed!")

print("Step 2: go to the website...")   
pyautogui.hotkey("ctrl", "t", interval=0.1)  # Open a new tab
time.sleep(1)
pyautogui.write("https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671", interval=0.15)  # Type the URL
time.sleep(1)
pyautogui.press("enter")  # Press Enter to go to the website

print("copy the full data from the website...")
pyautogui.hotkey("ctrl", "a")  # Select all content
time.sleep(1) 
pyautogui.hotkey("ctrl", "c")  # Copy the selected content
time.sleep(1)

# Step 4: Open Microsoft Word
print("Step 3: Opening note pad...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("notepad", interval=0.1)
pyautogui.press("enter")

time.sleep(5)

# Step 5: Paste the Python code into Word
print("Step 4: Pasting code into pad...")

pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# Step 6: Save the Word document
print("Step 5: Saving the notpad document...")

pyautogui.hotkey("ctrl", "s")
time.sleep(2)

# Enter the file name in the Save As dialog
pyautogui.write("PyAutoGUI_Code.docx", interval=0.05)
pyautogui.press("enter")

time.sleep(2)

print("Task completed!")





