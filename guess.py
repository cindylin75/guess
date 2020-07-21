import random
start = input('Please insert the initial number:')
end = input('Please insert the end number:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 #count=count+1
	num = input('Please guess your number:')
	num = int(num)
	if num == r:
		print('congrats!')
		print('this is your', count ,'times')
		break
	elif num > r:
		print('this number is over than the correct number')
	elif num < r:
		print('this number is less than the correct number')
	print('this is your', count ,'times')