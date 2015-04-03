# Import the required libraries.
import serial
import mosquitto

# Open port by name.
port = serial.Serial("COM3",9600,timeout=2) 
command = port.read()

# Create a client wrapper.
client = mosquitto.Mosquitto("DAT205")

# Connect to the broker.
client.connect("127.0.0.1")

# Subscribe to the lights topic.
client.subscribe("lights")

# Method to handle the incoming message.
def messageReceived(broker, obj, msg):
    global client
    
    # When the payload of an incoming message is "ON" switch the LED on.
    if msg.payload == "ON":
        port.write("S")
        
    # When the payload of an incoming message is "OFF" switch the LED off.    
    elif msg.payload == "OFF":
        port.write("D")
        
# Register the incoming message handler.
client.on_message = messageReceived

# when the client still exists, ask it to process incoming messages
while (client != None): client.loop()
 