import serial
import time
import re

class RelayAPI:

    def _RELAY2COM(self,RELAY:str):
        if(re.match(r'RELAY-\w\w\w+', RELAY)):
            RELAY="/dev/tty.usbserial-"+RELAY[6:]
        elif (re.match(r'RELAY-\d', RELAY)):             
            RELAY="COM"+RELAY[6:]
        return RELAY

    def Relay1_Open(self, RELAY, Seconds=0.1):    
        COM= self._RELAY2COM(RELAY)    
        sp = serial.Serial(COM, 115200, 8, 'N', 1)
        sp.write(bytes.fromhex('A00100A1'))
        time.sleep(float(Seconds))
        sp.close()

    def Relay1_Close(self, RELAY, Seconds=0.1):
        COM= self._RELAY2COM(RELAY)
        sp = serial.Serial(COM, 115200, 8, 'N', 1)
        sp.write(bytes.fromhex('A00101A2'))
        time.sleep(float(Seconds))
        sp.close()

    def Relay2_Open(self, RELAY, Seconds=0.1):
        COM= self._RELAY2COM(RELAY)
        sp = serial.Serial(COM, 115200, 8, 'N', 1)
        sp.write(bytes.fromhex('A00200A2'))
        time.sleep(float(Seconds))
        sp.close()

    def Relay2_Close(self, RELAY, Seconds=0.1):
        COM= self._RELAY2COM(RELAY)
        sp = serial.Serial(COM, 115200, 8, 'N', 1)
        sp.write(bytes.fromhex('A00201A3'))
        time.sleep(float(Seconds))
        sp.close()


