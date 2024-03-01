x = 169
if 100 < x < 999:
	print("x - trehznachnoe")
else:
	print("x - ne trehznachnoe")
if x >= 0:
	print("x - polojitelnoe")
else: 
	print("x - otrizatelnoe")
if x % 31 == 0:
	print("x - delitsya bez ostatka na 31")
else:
	print("x - ne delitsya bez ostatka na 31")

if (x > 100 and x % 17 == 0) or (x > 150 and x == 13 ** 2):
	print (x)