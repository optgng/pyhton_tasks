def TF_pаlindrome(number):
    number_copy = number
    result = 0
    while (number != 0):
        buf_number = number % 10
        result = result * 10 + buf_number
        number = int(number / 10)

    if result == number_copy:
        print(True)
    else:
        print(False)

if __name__ == "__main__" :
    num = int(input("Введите целое число: "))
    if num % 1 == 0:
        TF_pаlindrome(num)
    else:
        print("Введено не целое число...")