import paho.mqtt.client as paho
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO>IN, pull_up_down=GPIO.PUD_DOWN)

broker="broker.emqx.io"
port = 1883

def on_publish(client,userdata,result):
    print("data published \n")
    pass

while True:
    if GPIO.input(10) == GPIO.HIGH:
        firstclient = paho.client("led")
        firstclient.on_publish = on_publish
        firstclient.connect(broker, port)
        ret= firstclient.publish("led", "01")
