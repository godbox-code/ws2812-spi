
import sys
import os
import spidev
import numpy as np
from time import sleep

sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-9]) # get path of previous directory
from ws2812conrtoller import Ws2812Conrtoller

SPI_BUS = 1                     # Bus number of SPI device
SPI_DEVICE = 0                  # device number of SPI device

spi = spidev.SpiDev()           # Instantiate SPI device
spi.open(SPI_BUS,SPI_DEVICE)    # Open spi Device

ws2812 = Ws2812Conrtoller(spi)  #Instantiate Ws2812Conrtoller, pass SPI device to it

LEDS = 100                      # Number of leds

array = np.zeros([LEDS,3], dtype=np.uint8)    #set inital array, 256x3. dtype=np.uint8 is critical to avoid decimal points
while True:
    '''
    all leds start turned off.
    one buy one it will turn them on in order.
    once number 'LEDS' has been reached, one by one it will turn them off in order.
    color is set with  << np.array([255,0,0]).reshape([1,3]) >>
    the color the array is [green, red, blue]
    '''
    for count in range(LEDS):
        array[count,:] = np.array([255,0,0]).reshape([1,3])
        ws2812.send(array)
        sleep(0.1)
    for count in range(LEDS):
        array[count,:] = 0
        ws2812.send(array)
        sleep(0.1)



