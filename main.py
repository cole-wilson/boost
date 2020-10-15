from os import environ, system
import json, os

def ranges(nums,limit=999):
	nums = sorted(set(nums))
	gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
	edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
	z = list(zip(edges, edges))
	newz = []
	for x in z:
		if x[1]-x[0] > limit:
			prev = x[0]
			for o in range((x[1]-x[0])//limit):
				newz.append((prev,prev+limit))
				prev = prev + limit
			newz.append((prev,prev+(x[1]-x[0])%limit))
			prev = prev + (x[1]-x[0])%limit
			
		else:
			newz.append(x)
	return newz

def pretty(d, indent=0):
	 print(json.dumps(d, sort_keys=True, indent=4))

# print(ranges([1,2,3,4,6,7,8,9,10]))
rows, columns = os.popen('stty size', 'r').read().split()
size = '8x10'
message = input(">>>").replace('. ','.')

letterheight = int(size.split('x')[1])
spaceamount = 2

added = []

# MAKE MESSAGE
for x in range(0,letterheight):
	thisline = ''
	for letter in message:
		letter = letter.upper()
		if letter == ' ':
			letter = 'space'
		elif letter == '.':
			letter = 'period'
		thisline = thisline + open('letters/'+size+'/'+letter).read().split('\n')[x]+(' _'*spaceamount)+(' ' if spaceamount != 0 else ' ')
	added.append(thisline)

# SAVE MESSAGE
f = open('oput.py','w+')
f.write('content = """\n')
for x in added:
	f.write(x+'\n')
f.write('"""\n')
f.close()

# EDIT MESSAGE
if environ.get('NANO') is None:
	system('sudo nano oput.py')

# LOAD oput
import oput

c = oput.content.split('\n')[1:-1]
# FIND LINES GOING SIDE TO SIDE
sidetosidelines = {}


po = False
if len(c[0]) <= int(columns):
	po = True

for y in range(len(c)):
	xs = []
	count = -1
	for x in range(0,len(c[y]),2):
		if po:
			print(c[y][x]+' ',end="")
		count = count + 1
		if c[y][x] == "@":
			xs.append(count)
	if po:
		print('')
	sidetosidelines[y] = xs

# TRANSPOSE output
c2 = []
for x in range(len(c[0])):
	lineadd = ""
	for y in range(len(c)):
		lineadd = lineadd + c[y][x]
	c2.append(lineadd)
c = c2

# FIND LINES GOING UP AND DOWN
updownlines = {}
cou = -1
for y in range(0,len(c),2):
	cou = cou + 1
	xs = []
	count = -1
	for x in range(0,len(c[y])):
		# print(c[y][x],end="")
		count = count + 1
		if c[y][x] == "@":
			xs.append(count)
	# print('')
	updownlines[cou] = xs



# GET RID OF DOTS
dots = []

sides = {}
for x in sidetosidelines.keys():
	sides[x] = []
	sidetosidelines[x] = ranges(sidetosidelines[x],limit=8)
	for ix in sidetosidelines[x]:
		if ix[0] != ix[1]:
			sides[x].append(ix)
		else:
			dots.append(ix)

ups = {}
for x in updownlines.keys():
	ups[x] = []
	updownlines[x] = ranges(updownlines[x],limit=10)
	for ix in updownlines[x]:
		if ix[0] != ix[1] or ix in dots:
			ups[x].append(ix)

# NOW WE HAVE sides AND ups
print('---')
print(sides)
print('---')
print(ups)

# PRINT

import brick
print('Startings')
xcount = -1
while True:
	xcount = xcount + 1
	# print('Resetting...')
	# brick.sety(0)
	print('Pen up')
	brick.penup()
	print(f'Scanning for up and down lines at x position {xcount}')
	for x in ups[xcount]:
		print(f'Drawing from y{x[0]} to y{x[1]}.')
		brick.sety(x[0])
		brick.pendown()
		brick.sety(x[1])
		brick.penup()
	for y in range(10):
		for x in sides[y]:
			if x[0] == xcount:
				print(f'Drawing from x{x[0]} to x{x[1]}.')
				brick.sety(y)
				brick.pendown()
				for inc in range(x[1]-x[0]):
					brick.movex(2)
				for inc in range(x[1]-x[0]):
					brick.movex(-2)
				brick.penup()
	brick.movex(2)
