def rever_number(num):
    rev_num = 0
    while num != 0:
        digit = num % 10
        num = num // 10
        rev_num = rev_num * 10
        rev_num = rev_num + digit
    print("Обратное число: ", rev_num, end='')

if __name__ == "__main__" :
    number = int(input("Введите целое число: "))
    rever_number(number)
    