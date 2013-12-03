# conding =utf8
number = 23
running = True
while running:
	guess = int(input('请输入一个整数: '))
	if guess == number:
		print('恭喜,你猜对了。') #新块从这里开始
		print('(但你没有获得任何奖品)') #新块在这里结束
		running = False
	elif guess < number:
		print('不对，你猜得有点儿小') #另一块
		#在一个块中你可以做你想做的任何事...
	else:
		print('不对，你猜得有点大')
		#你猜的数比number大时才能到这里
else:
	print('While循环结束。')

print('完成')
#if语句执行完后，最后的语句总是被执行