# bounce.py
#
# Exercise 1.5
height = 100 # meter
bounce_ratio = 3.0/5.0

for i in range(1, 11):
	height = height * bounce_ratio
	print(f"{i} {round(height, 4)}")