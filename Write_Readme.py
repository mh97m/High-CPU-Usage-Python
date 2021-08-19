from pynput import mouse,keyboard

key = keyboard.Controller()
key.press(keyboard.Key.ctrl)
key.press(keyboard.Key.cmd)
key.press('d')


'''m.press(keyboard.Key.cmd)
m.release(keyboard.Key.cmd)
m.release(keyboard.Key.cmd)
'''