def simple_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
    return True 


if __name__ == "__main__" :
    number = int(input("Введите целое число от 0 до 100000: "))
    if(number >= 0 and number <= 100000):
        print(simple_number(number))
    else:
        print("Некорректное число...")