from pylgbst.hub import MoveHub
from pylgbst import get_connection_gatt

conn = get_connection_gatt(hub_mac="00:16:53:A6:60:CC")
hub = MoveHub(conn)

p = 0
y = 0
x = 0

def penup():
	global p
	if p!=0:
		hub.motor_A.angled(40,0.2)
		p = 0
def pendown():
	global p
	if p!=1:
		hub.motor_A.angled(-40,0.2)
		p = 1
def movex(amount):
	global x
	hub.motor_B.angled(5*amount,0.2)
	x = x + amount
def setx(amount):
	global x
	movex(amount-x)
def movey(amount):
	global y
	hub.motor_external.angled(10*amount,0.2)
	y = y + amount
def sety(amount):
	global y
	movey(amount-y)
