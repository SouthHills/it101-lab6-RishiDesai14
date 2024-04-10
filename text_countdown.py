from sense_emu import SenseHat
from time import sleep

sense_emulator = SenseHat()
R = [255, 0, 0]
G = [0, 255, 0]
purple = [128, 0, 128]

red_value = [100, 100, 100]

num = 9
for i in reversed(range(num+1)):
    sleep(1)
    if i == 0:
        sense_emulator.show_letter(f'{i}', purple)
    else:
        
        red_value[0] += 9
        red_value[1] -= 6
        red_value[2] -= 6
        sense_emulator.show_letter(f'{i}', red_value)
