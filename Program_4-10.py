def main():
	
	print('This program displays a list of numbers')
	print('(starting at 1) and their squares.')
	end = int(input('How high should i go? '))

	
	print()
	print('Number\tSquares')
	print('---------------')

	
	for number in range(1, end + 1):
		square = number**2
		print(number, '\t', square)


main()
