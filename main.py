import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

humtempSensor = 20
ldrSensor = 16

pumpRelay = 13
fanRelay = 19
lightRelay = 26

pumpRelaySts = 0
fanRelaySts = 0
lightRelaySts = 0

GPIO.setup(humtempSensor, GPIO.IN)   
GPIO.setup(ldrSensor, GPIO.IN)

GPIO.setup(pumpRelay, GPIO.OUT)   
GPIO.setup(fanRelay, GPIO.OUT) 
GPIO.setup(lightRelay, GPIO.OUT) 

GPIO.output(pumpRelay, GPIO.LOW)
GPIO.output(fanRelay, GPIO.LOW)
GPIO.output(lightRelay, GPIO.LOW)
	
@app.route("/")
def index():

	pumpRelaySts = GPIO.input(pumpRelay)
	fanRelaySts = GPIO.input(fanRelay)
	lightRelaySts = GPIO.input(lightRelay)

	deviceStatus = {
      		'pumpRelay'  : pumpRelaySts,
      		'fanRelay'  : fanRelaySts,
      		'lightRelay'  : lightRelaySts,
      	}

	return render_template('index.html', **deviceStatus)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):

	if deviceName == 'pumpRelay':
		actuator = pumpRelay
	if deviceName == 'fanRelay':
		actuator = fanRelay
	if deviceName == 'lightRelay':
		actuator = lightRelay
   
	if action.lower() == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action.lower() == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	pumpRelaySts = GPIO.input(pumpRelay)
	fanRelaySts = GPIO.input(fanRelay)
	lightRelaySts = GPIO.input(lightRelay)
   
	deviceStatus = {
      		'pumpRelay'  : pumpRelaySts,
      		'fanRelay'  : fanRelaySts,
      		'lightRelay'  : lightRelaySts,
	}
	return render_template('index.html', **deviceStatus)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)