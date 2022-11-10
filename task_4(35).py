def n_root(number, power):
    epsilon = 1e-10
    float 
    next_num = number
    while True:
        prev_num = next_num
        next_num = (prev_num*(power - 1) + number / pow(prev_num, power- 1))/power
        if abs(next_num - prev_num) > epsilon:
            continue
        else:
            break
    print("Корень ", power, "-ой степени: ", next_num)

if __name__ == "__main__" :
    number = float(input("Введите число: "))
    power = int(input("Введите степень корня: "))
    n_root(number, power)