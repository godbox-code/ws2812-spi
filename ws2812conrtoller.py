import numpy as np

class Ws2812Conrtoller():
    def __init__ (self, spi, array=None):
        self.spi = spi
        self.array = array
        if isinstance(self.array, np.ndarray):
            self.send(self.array)

    def send(self, array):
        d = np.array(array).ravel()
        tx = np.zeros(len(d)*4, dtype=np.uint8)
        for ibit in range(4):
          tx[3-ibit::4]=((d>>(2*ibit+1))&1)*0x60 + ((d>>(2*ibit+0))&1)*0x06 + 0x88
        tx = np.insert(tx, 0, 0x00)
        self.spi.max_speed_hz = int(4/1.05e-6)
        self.spi.writebytes(tx.tolist())
        return
