import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Time-and-sales")

def on_message(client, userdata, msg):
    print(str(msg.payload))

client = mqtt.Client("test")
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 7890)
client.loop_forever()