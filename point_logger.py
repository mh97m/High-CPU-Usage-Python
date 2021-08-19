from pynput import mouse
from pynput import keyboard
import threading 
def mouse_log(x , y , button , pressed):
    if pressed == True:
        print(x,y,button,pressed)

def mouse_start():
    with mouse.Listener(on_click = mouse_log) as lstn:
        lstn.join()
def keyboard_log(key):
    if type(key) == keyboard._win32.KeyCode:
        key = key.char
    else:
        key = ' ' + str(key) + ' '
    print(key)


def keyboard_start():
    with keyboard.Listener(on_press = keyboard_log) as lstn:
        lstn.join()
t1 = threading.Thread(target = keyboard_start,name = 'keyboard_start')
t2 = threading.Thread(target = mouse_start,name = 'mouse_start')
t1.start()
t2.start()
t1.join()
t2.join()

def frmt(j):
	for i in range(5):
		print(f'{j}'.center(20 , '_'))


'''for i in range(20):
	t = threading.Thread(target = frmt,name = f'{i}',args=(i,))
	print('{} is created'.format(t.name))
	t.start()
	print('{} is started'.format(t.name))'''
