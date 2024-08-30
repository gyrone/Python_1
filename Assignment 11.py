user_input = input('Enter a positice interger: ')

while True:
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break
        else:
            user_input + input('the bumber must be a positive interger. Enter again')

    else:
        user_input + input("invalid number. Please enter positive number")

print('collatz sequence: ')

while number != 1:
    print(number, end='->')
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
print(1)