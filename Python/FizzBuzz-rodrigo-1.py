for number in range(1,101):
	if (number%3 == 0) and (number%5 == 0):
		print(f"number {number}  - FizzBuzz")
	elif number%3==0 :
		print(f"number {number}  - Fizz")
	elif number%5==0 :
		print(f"number {number}  - Buzz")
	else:
		print(f"number {number}")