# NTCUSB

- ### NTC10 Temperature Sensor on RPi Pico

Copy main.py to RPi Pico.

Connect the NTC100 sensor to the ADC RPi Pico port using wiring diagram below.

 - ### Wiring diagram
```
                                  NTC10
RPi Pico  [GP28 Pin 28]----------/\/\/\--------- [AGND Pin 33] 
                                  10k
RPi Pico  [GP28 Pin 28]----------/\/\/\--------- [VCC Pin 36] 
```

Connect PC with the RPi Pico together with the USB cable.
Select proper serial port number in terminal configuration or use ntc_usb_gui.py to show measured values in the pop-up window on Windows, MacOS or Linux
