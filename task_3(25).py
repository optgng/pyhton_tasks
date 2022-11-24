def rever_number(num):
    rev_num = 0
    if num > 0:
        while (num != 0):
            digit = int(num % 10)
            rev_num = rev_num * 10 + digit
            num = int(num / 10)
        print("Обратное число: ", rev_num, end='')
    else:
        num = abs(num)
        while (num != 0):
            digit = int(num % 10)
            rev_num = rev_num * 10 + digit
            num = int(num / 10)
        print('Обратное число: -' + str(rev_num))

if __name__ == "__main__" :
    number = int(input("Введите целое число: "))
    rever_number(number)
    