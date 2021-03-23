import random

start = input('請輸入起始數字: ')
end = input('請輸入結束數字: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	num = input('請猜數字: ')
	num = int(num)
	count = count + 1
	if num == r:
		print('你猜中了')
		print('共猜了', count, '次')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	print('共猜了', count, '次')