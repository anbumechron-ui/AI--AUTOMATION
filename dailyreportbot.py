
import os
import time
import datetime
import subprocess

import pyautogui
import pyperclip


# ==================================================
# SOCIAL EAGLE - GEN AI ARCHITECT PROGRAM
# Assignment 1: PyAutoGUI Daily Report Automation
# ==================================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# Output folder on Desktop
OUTPUT_FOLDER = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "Daily_Report_Output"
)

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Automatically generate date and time
now = datetime.datetime.now()

date_time = now.strftime("%Y-%m-%d %H:%M:%S")
today = now.strftime("%Y-%m-%d")

excel_path = os.path.join(
    OUTPUT_FOLDER,
    f"daily_report_{today}.xlsx"
)

screenshot_path = os.path.join(
    OUTPUT_FOLDER,
    f"daily_report_screenshot_{today}.png"
)

# Concise weather information for Vellore
weather_url = (
    "https://wttr.in/Vellore"
    "?format=%l:+%c+%t+feels+like+%f+humidity+%h"
)


def open_chrome_and_fetch_weather():
    """Open Chrome and copy the weather information."""

    print("\nStep 1: Opening Chrome...")

    pyautogui.hotkey("win", "r")
    time.sleep(2)

    pyautogui.write("chrome", interval=0.1)
    pyautogui.press("enter")

    time.sleep(8)

    print("Step 2: Opening Vellore weather page...")

    pyautogui.hotkey("ctrl", "l")
    pyperclip.copy(weather_url)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    time.sleep(12)

    print("Step 3: Copying weather information...")

    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)

    weather_data = pyperclip.paste().strip()
    weather_data = " ".join(weather_data.split())

    if not weather_data:
        weather_data = "Weather data unavailable"

    print("Weather information:", weather_data)

    return weather_data


def open_excel_and_create_report(weather_data):
    """Open Excel, create a workbook, and save the report."""

    print("\nStep 4: Opening Microsoft Excel...")

    # Remove today's previous output to avoid overwrite dialogs
    if os.path.exists(excel_path):
        os.remove(excel_path)

    pyautogui.hotkey("win", "r")
    time.sleep(2)

    pyautogui.write("excel", interval=0.1)
    pyautogui.press("enter")

    # Allow Excel time to start
    time.sleep(15)

    print("Step 5: Creating a new workbook...")

    # Create a blank workbook
    pyautogui.hotkey("ctrl", "n")
    time.sleep(8)

    # Move to the first worksheet cell
    pyautogui.press("esc")
    pyautogui.hotkey("ctrl", "home")
    time.sleep(2)

    # Prepare the three-column report
    headers = "Date & Time\tFetched Data\tComment"

    row = (
        f"{date_time}\t"
        f"{weather_data}\t"
        "Vellore weather update recorded automatically"
    )

    report = headers + "\n" + row

    # Paste into Excel
    pyperclip.copy(report)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(5)

    print("Step 6: Saving the Excel workbook...")

    # Open Save As
    pyautogui.press("f12")
    time.sleep(5)

    # Enter the complete file path
    pyperclip.copy(excel_path)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    time.sleep(8)

    print("Step 7: Capturing the screenshot...")

    # Ensure the Excel window is visible before capturing
    pyautogui.screenshot().save(screenshot_path)

    print("\nREPORT CREATED")
    print("Excel file:", excel_path)
    print("Screenshot:", screenshot_path)


def main():
    print("=" * 50)
    print("DAILY REPORT AUTOMATION STARTED")
    print("=" * 50)

    print("Date and time:", date_time)

    try:
        weather_data = open_chrome_and_fetch_weather()

        open_excel_and_create_report(weather_data)

        print("\nAutomation finished.")
        print("Please verify the Excel file and screenshot.")

    except Exception as error:
        print("\nAutomation failed:", error)

    print("\nOutput folder:", OUTPUT_FOLDER)


if __name__ == "__main__":
    main()
