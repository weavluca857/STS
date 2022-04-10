import keyboard

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('w'):  # if key 'q' is pressed
            print("W has been pressed")
            break  # finishing the loop
    except:
        break