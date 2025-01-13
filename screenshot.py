from pynput import keyboard
from PIL import ImageGrab
import time
import sys 
import plyer

sys.stderr = open('error_log.txt', 'w')

# all pressed keys 
pressed_keys = set()

def on_press(key):
    print(f"on_press: {key}")
    try:
        pressed_keys.add(key)
        
        if (keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys) \
            and (keyboard.Key.alt_l in pressed_keys or keyboard.Key.alt_r in pressed_keys) \
            and (keyboard.KeyCode.from_vk(80)): 
            #vk(80) = p char
            time.sleep(0.08)
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            #take the screenshot
            print("Taking screenshot...")
            screenshot = ImageGrab.grab()
            #save ss
            screenshot.save('screenshot_ ' + str(timestamp) +'_.png')
            print("Screenshot saved!")
            #send notification
            plyer.notification.notify(
                title='Captura de Pantalla',
                message='Se ha tomado una captura de pantalla :)',
                app_name='ScreenshotApp'
            )
        else: 
            print("Not taking any screenshot")
    except Exception as e:
        print(f"An error occurred: {e}")

def on_release(key):
    print(f"on_release: {key}")
    try:
        # remove the key from pressed keys set
        pressed_keys.remove(key)
    except KeyError:
        pass
    
def start_listener():
    # inicial el listener para las teclas
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()


while True: 
    start_listener()
    time.sleep(1) # para evitar que el script se bloquee