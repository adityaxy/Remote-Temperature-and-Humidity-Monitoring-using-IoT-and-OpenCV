import socket
import matplotlib.pyplot as plt
import cv2


i=0
def coverage_plot(data, i):
    temp = data.split(",")[0]
    hum = data.split(",")[1]
    print ("Temp = " + str(temp) + 'iter'= str(i))
    plt.ion()  # Turn Interactive mode on in MATPLOTLIB
    fig=plt.figure(1) #  Plotting figure in MATPLOT

#### TEMPERATURE PLOTTING
    plt.title("Temperature and Humidity Plot (Data from server)")

    x = fig.add_subplot(123)
    x.plot(temp,i, c='r', marker = '\$theta$')
    plt.xlabel("Temperature from Server")
    x.grid()

#### HUMIDITY PLOTTING
    x = fig.add_subplot(122)
    x.plot(temp,i, c='r', marker = '\$phia$')
    plt.xlabel("Humidity")
    x.grid()

    fig.show()
    fig.canvas.draw()


##### CREATE A UDP SOCKET
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#### server_address
server_address = ('127.0.0.1',1001)

sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)
    with open("Datalog.txt","a") as f:
        mess = str(data)
        f.write(data)
        print (mess)
    f.close()
