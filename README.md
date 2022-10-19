# NTCUSB

- ### NTC10 Temperature Sensor on RPi Pico

Copy main.py to RPi Pico.

Connect the NTC10 sensor to the ADC RPi Pico port using wiring diagram below.

 - ### Wiring diagram
```
                                  NTC10
RPi Pico  [GP28 Pin 28]----------/\/\/\--------- [AGND Pin 33] 
                                  10k
RPi Pico  [GP28 Pin 28]----------/\/\/\--------- [VCC Pin 36] 
```

Connect PC with the RPi Pico together with the USB cable.
Select proper serial port number in terminal configuration or use ntc_usb_gui.py to show measured values in the pop-up window on Windows, MacOS or Linux Operating Systems.

## B.o.M - Bill of Materials

* [NTC10](https://botland.store/search?s=ntc10) - 1 pcs
* [Raspberry Pico](https://botland.store/raspberry-pi-pico-modules-and-kits/18767-raspberry-pi-pico-rp2040-arm-cortex-m0-0617588405587.html) - 1 pcs
* [RPi Pico and Sensor Case](https://www.tme.eu/pl/en/details/pp73g/enclosures-for-alarms-and-sensors/supertronic/) - 1 pcs
* [MicroUSB B-A cable](https://botland.store/usb-20-cables/6417-microusb-b-a-cable-in-white-braid-esperanza-eb181w-2m-5901299920107.html) - 1 pcs
