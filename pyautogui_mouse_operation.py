import pyautogui
import time

#mouse operations
pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second
pyautogui.click()  # Click the mouse at the current position
pyautogui.doubleClick()  # Double-click the mouse at the current position
pyautogui.rightClick()  # Right-click the mouse at the current position
pyautogui.dragTo(200, 200, duration=1)  # Drag the mouse to (200, 200) over 1 second
pyautogui.scroll(500)  # Scroll up 500 units
