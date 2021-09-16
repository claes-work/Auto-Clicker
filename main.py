import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

button = Button.left

# delay in seconds
delay = 10

# start and stop key
start_stop_key = KeyCode(char='s')

# exit key
exit_key = KeyCode(char='e')

# ClickMouse class
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # set running to true what will indicating that the script is still running
    def start_clicking(self):
        self.running = True


    # set running to true what will indicating that the script should stop
    def stop_clicking(self):
        self.running = False


    # call the stop_clicking() method and set the program_running attribute to false
    def exit(self):
        self.stop_clicking()
        self.program_running = False


    # while the program_running attribute is true click the mouse button every x seconds
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# initiating a new ClickMouse class
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

# start or stop clicking based on the key that is getting pressed
def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


# define listener
with Listener(on_press=on_press) as listener:
    listener.join()
