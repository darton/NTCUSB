from machine import Pin, ADC
from utime import sleep_ms
import math as mt


def led_blinking(on_time, off_time, number_of_blinks):
    led = machine.Pin(25, machine.Pin.OUT)
    led.value(0)
    for _ in range(number_of_blinks):
        led.toggle()
        sleep_ms(on_time)
        led.toggle()
        sleep_ms(off_time)    
    

def ntc(adc_pin):
    Vout_adc = ADC(adc_pin)
    Vout = Vout_adc.read_u16() * 3.3 / 65536
    Ro = 9989 # 10k resistor
    Vin = 3.3 # V
    # Steinhart Constants
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    # Calculate Resistance
    Rt = (Vout * Ro) / (Vin - Vout)
    # Steinhart - Hart Equation
    TempK = 1 / (A + (B * mt.log(Rt)) + C * mt.pow(mt.log(Rt),3))
    # Convert from Kelvin to Celsius
    return int(round(round(TempK,2) - 273.15,2) * 100)
    

while True:
    ntc1_tempC = ntc(adc_pin = 28)
    #ntc2_tempC = ntc(adc_pin = 27)
    #ntc3_tempC = ntc(adc_pin = 26)
    print(f'NTC1 {ntc1_tempC}')
    #print(f'NTC2 {ntc2_tempC}')
    #print(f'NTC3 {ntc3_tempC}')
    led_blinking(700,1300,1)
