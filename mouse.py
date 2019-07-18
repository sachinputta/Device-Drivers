from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

o = mouse.position
n = mouse.position
while(1):
    n = mouse.position
    if o != n:
        print(mouse.position)
        o = n
