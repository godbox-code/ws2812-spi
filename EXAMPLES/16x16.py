
import sys
import os
import spidev
import numpy as np
from time import sleep
from random import randint

sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-9]) # get path of previous directory
from ws2812conrtoller import Ws2812Conrtoller

SPI_BUS = 1                     # Bus number of SPI device
SPI_DEVICE = 0                  # device number of SPI device

spi = spidev.SpiDev()           # Instantiate SPI device
spi.open(SPI_BUS,SPI_DEVICE)    # Open spi Device

ws2812 = Ws2812Conrtoller(spi)  #Instantiate Ws2812Conrtoller, pass SPI device to it


'''
in this example the leds area a 16x16 LED matrix.
so i can address the leds easily i use a 16x16x3 matrix.
array[1,1,:] will corrospond to the led on row2, coloum2 (array is zero indexed)
'''
array = np.zeros([16,16,3], dtype=np.uint8)    #set inital array

def fix_matrix(array):
    '''
    the 16x16 LED matrix actualy snakes down the panel \n
    in row 0 the first led is in colum 0\n
    but in row 1 the first led is actualy in colum 15\n
    this function just flips every second row so the output is correct\n
    '''
    array[::2, :,:] = array[::2, ::-1,:]
    return array


while True:
    '''
    LED in col is turned on at a random color
    every loop, the previous col is turned off, and the next one turned on
    '''

    for col in range(16):
        for row in range(16):
            array[row,col,:] = np.array([randint(0,255),randint(0,255),randint(0,255)]).reshape([1,1,3])
            array[row,col-1,:] = 0
        ws2812.send(fix_matrix(np.copy(array)))     # send a copy of the array, otherwise fix_matrix() will apply to array
        sleep(0.2)



