import pyautogui
import keyboard
import time

need_bubbles = ['images/thirsty.png', 'images/bored.png', 'images/hungry.png', 'images/infested.png']
default_cooldown = 0.5
exit_key = 'p'

def locate_needy_plants(image):
    try:
        locations = list(pyautogui.locateAllOnScreen(image, confidence=0.90, grayscale=True))
        if locations:
            return locations
    except:
        return None

def help_needy_plant(location):
    x, y = location
    pyautogui.moveTo(x - 100, y + 50)
    pyautogui.press('q')
    time.sleep(0.1)
    pyautogui.click()


time.sleep(3)
while not keyboard.is_pressed(exit_key):
    for bubble in need_bubbles:
        plant_locations = locate_needy_plants(bubble)
        if plant_locations:
            for plant_location in plant_locations:
                print(f"Found image: {bubble} at {plant_location}")
                help_needy_plant(pyautogui.center(plant_location))
            time.sleep(0.5)
        else:
            print("No needy plants found.")
    time.sleep(default_cooldown)
