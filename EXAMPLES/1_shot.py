
import sys
import os
import spidev
import numpy as np
from random import randint

sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-9]) # get path of previous directory
from ws2812conrtoller import Ws2812Conrtoller

SPI_BUS = 1
SPI_DEVICE = 0

spi = spidev.SpiDev()           # Instantiate SPI device
spi.open(SPI_BUS,SPI_DEVICE)    # Open spi Device

LEDS = 100                      # Number of leds

array = np.zeros([LEDS,3], dtype=np.uint8)      #set inital array, 256x3. dtype=np.uint8 is critical to avoid decimal points

for _ in range(20):
    '''
    20 randon points are picked from the list. >> array[randint(0,LEDS-1),:] <<
    a random color is assigned to each point >> np.array([randint(0,255),randint(0,255),randint(0,255)]).reshape([1,3]) <<
    '''
    array[randint(0,LEDS-1),:] = np.array([randint(0,255),randint(0,255),randint(0,255)]).reshape([1,3])


Ws2812Conrtoller(spi, array)  #Instantiate Ws2812Conrtoller, pass SPI device to it and pass the array




