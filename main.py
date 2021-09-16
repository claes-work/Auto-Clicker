import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 10
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):

    def start_clicking(self):

    def stop_clicking(self):

    def exit(self):

    def run(self):