import machine
import utime
import neopixel

neoString = neopixel.NeoPixel(machine.Pin(8), 20)
analog_value_x = machine.ADC(28)
analog_value_y = machine.ADC(27)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

neoString.fill((100,0,0))
neoString.write()
 
while True:
    reading_x = analog_value_x.read_u16()     
    reading_y = analog_value_y.read_u16()
    reading_button = button.value()     
    print(f"ADC: {reading_x}, {reading_y}, {reading_button}")
    utime.sleep(0.2)
