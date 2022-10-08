import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os
import time
import json

a_file = open("test.json", "r")
data = a_file.read()
#json_object = json.loads(data)

print(data)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("led", 0)
   
   

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")
    print(msg.payload)
    if(msg.payload == b'01'):
        print("Library LED is on")
        GPIO.output(18, GPIO.HIGH)
    else if(msg.payload == b'02'):
        print("gymnasium LED is on")
        GPIO.output(18, GPIO.HIGH)
    else if(msg.payload == b'03'):
        print("auditorium LED is on")
        GPIO.output(18, GPIO.HIGH)
    else if(msg.payload == b'04'):
        print("lecture1 LED is on")
        GPIO.output(18, GPIO.HIGH)
    else if(msg.payload == b'05'):
        print("lecture2 LED is on")
        GPIO.output(18, GPIO.HIGH)
    else:
        print("LED is off")
        GPIO.output(18, GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.will_set('raspberry/status', b'{"status": "Off"}')


client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()
