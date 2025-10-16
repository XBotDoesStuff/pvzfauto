import pyautogui
import keyboard
import time

time.sleep(3)
image = "button.png"

recent_clicks = []
cooldown = 0.5
tolerance_radius = 10

while not keyboard.is_pressed("p"):
    location = pyautogui.locateCenterOnScreen(image, confidence=0.8)
    
    if location is not None:
        too_close = False
        for (x, y, t) in recent_clicks:
            if abs(location.x - x) < tolerance_radius and abs(location.y - y) < tolerance_radius and (time.time() - t) < cooldown:
                too_close = True
                break

        if not too_close:
            print(f"Found at {location}, watering...")
            pyautogui.moveTo(location.x - 50, location.y + 50)
            time.sleep(0.1)
            pyautogui.press("q")
            pyautogui.click(location.x - 50, location.y + 50)
            recent_clicks.append((location.x, location.y, time.time()))
        else:
            print("Skipping — just watered here.")
        
        time.sleep(0.2)
    else:
        print("No thirsty plants found, retrying...")
        time.sleep(0.5)

print("Program terminated successfully.")
