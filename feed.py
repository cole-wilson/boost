import brick
brick.penup()
brick.hub.motor_B.start_speed(0.5)
input('Press enter to stop')
brick.hub.motor_B.stop()