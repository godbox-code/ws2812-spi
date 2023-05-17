# ws2812conrtoller.py

A simple python class that uses a NumPy array control the WS2812 RGB LED chips on the OrangePi using the hardware SPI MOSI (so no other hardware is needed). </p>

### Why?

I wanted an easy, low overhead way of manually controlling leds. FastLED/Adafruit_NeoPixel are great at what they do, but using them to manually set colors is overkill.</p>

As the WS2812 communication needs strict timing, the DIN line cannot be driven from a normal GPIO line with python (an interrupt on the raspberry would screw things up). Thats' why this class uses the hardware SPI MOSI line, this does confirm to the timing requirements.</p>

This code was simplified from: https://github.com/mcgurk/ws2812-spi <br>
More info on the WS2812: https://wp.josh.com/2014/05/13/ws2812-neopixels-are-not-so-finicky-once-you-get-to-know-them/ <br>



# Orange Pi
Tested on: <br>
Orange Pi 3 LTS, <br>

```
$ uname -a
Linux orangepi3-lts 5.16.17-sun50iw6 #3.0.8 SMP Tue Sep 6 20:11:50 CST 2022 aarch64 GNU/Linux
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux 11 (bullseye)
Release:	11
Codename:	bullseye
``` 
</p>
should work on most orangepi/Raspberry Pi 


# Python and modules


```
sudo apt install python3-pip python3-setuptools python3-dev python3-wheel python3-numpy
sudo pip3 install spidev
```

# SPI SETUP


### Enable SPI


SPI is not enabled by default on the OrangePi.

```
sudo orangepi-config

```

System -> BootEnv -> spi-spidev<br>
append the following to the end of the options


```
overlays=spi-spidev1
```

Save->Install->Ok(install/update bootloader)->Back->Exit<br>
reboot<br>


### Test

check to make sure the above changes worked

```
$ ls /dev | grep spi

spidev1.0
```

if output is blank, something went wrong, start again.<br>
note: spidev[BUS_NUMBER].[DEVICE_NUMBER] bus/device numbers are used to instantiate the SPI device and can differ from my output

### Allow access to spidev from userspace

make a group that will have acess to spidev, and add the current user to that group:<br>

```
sudo groupadd spiuser
sudo adduser "$USER" spiuser
```

make a udev rule that will add spidev to the group:<br>

```
sudo nano /etc/udev/rules.d/50-spi.rules
```

add the following line to the new rule file

```
SUBSYSTEM=="spidev", GROUP="spiuser", MODE="0660"
```

reboot


# Test

Run one of the programs in EXAMPLES folder

