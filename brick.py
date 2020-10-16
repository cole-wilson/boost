from pylgbst.hub import MoveHub, Voltage, VisionSensor
from pylgbst import get_connection_gatt

color = 0

def callback(clr,distance):
	global color
	color = clr
	print(color)


conn = get_connection_gatt(hub_mac="00:16:53:A6:60:CC")
hub = MoveHub(conn)
hub.vision_sensor.unsubscribe(callback)

hub.vision_sensor.subscribe(callback, mode=VisionSensor.COLOR_DISTANCE_FLOAT)


p = 0
y = 0
x = 0
mult=0.6
def penup():
	global p
	if p!=0:
		hub.motor_A.angled(40,0.8)
		p = 0
def pendown():
	global p
	if p!=1:
		hub.motor_A.angled(-40,0.8)
		p = 1
def movex(amount):
	global x
	global mult
	hub.motor_B.angled((4*mult)*amount,0.8)
	x = x + amount
def setx(amount):
	global x
	movex(amount-x)
def movey(amount):
	global y
	global mult
	hub.motor_external.angled((24*mult)*amount,0.8)
	y = y + amount
def sety(amount):
	global y
	movey(amount-y)