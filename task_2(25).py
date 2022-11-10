def manage_num(array):
    arr_2 = []
    arr_3 = []
    arr_5 = []
    
    for i in range(len(array)):
        if array[i] % 2 == 0:
            arr_2.append(array[i])
        if array[i] % 3 == 0:
            arr_3.append(array[i])
        if array[i] % 5 == 0:
            arr_5.append(array[i])
    
    print("Числа, которые делятся на 2: ", end='')
    for i in range(len(arr_2)):
        print(arr_2[i], end=" ")
    print('\n')
    
    print("Числа, которые делятся на 3: ", end='')
    for i in range(len(arr_3)):
        print(arr_3[i], end=" ")
    print('\n')    
    
    print("Числа, которые делятся на 5: ", end='')
    for i in range(len(arr_5)):
        print(arr_5[i], end=" ")     

if __name__ == "__main__" :
    start_array = []
    inp_num = int(input("Введите кол-во элементов списка: "))

    for i in range(inp_num):
        print("Введите значение: ", end='')
        start_array.append(int(input()))

    manage_num(start_array)

