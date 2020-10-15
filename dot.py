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
		elif letter == ',':
			letter = 'comma'
		elif letter == '?':
			letter = 'question'
		elif letter == '!':
			letter = 'exclamation'
		elif letter == "'":
			letter = 'apostrophe'
		
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


# TRANSPOSE output
c2 = []
for x in range(len(c[0])):
	lineadd = ""
	for y in range(len(c)):
		lineadd = lineadd + c[y][x]
	if lineadd.replace(' ','') != "":
		c2.append(lineadd.replace(' ',''))
c = c2

import brick

lasty = 0
for x in c:
	count = 0
	for y in x:
		count = count + 1
		if y == '@':
			if lasty != y and lasty+1 != y and lasty-1 != y:
					brick.penup()
			else:
				lasty = y
				print('movingy')
			brick.sety(count)
			brick.pendown()
	brick.movex(2)