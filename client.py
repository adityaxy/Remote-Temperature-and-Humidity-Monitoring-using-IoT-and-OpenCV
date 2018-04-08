import RPi.GPIO as GPIO
import socket
from time import sleep
import Adafruit_DHT


#### Reading Sensor Data From DHT22

def sensordata():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    sensor = GPIO.Adafruit_DHT.AM2302
    humidity,temperature =  Adafruit_DHT.read_retry(sensor,4) #PIN 4 iv in BCM Mode

    return (humidity, temperature)

### CREATING UDP SOCKET

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

### IP ADDRESS OF SERVER

server_address = ('127.0.0.1',1001)

try :
    while True:
        humid, temp = sensordata()
        message = str(humid) + "," + str(temp)
        print ("Sending Data to server")
        sent = sock.sendto(message,server_address)
finally:
    sock.close()
