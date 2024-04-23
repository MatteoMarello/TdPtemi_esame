def dichotomic(input_list, value):
    if len(input_list) == 0:
        return False
    if len(input_list) == 1:
        if input_list[0] == value:
            return True
        else:
            return False
    else:
        i = len(input_list) // 2
        return (dichotomic(input_list[:i], value) or dichotomic(input_list[i:], value))


sequenza = [1,2,3,4,5,6,7,8]
print(dichotomic(sequenza, 2))
print(dichotomic(sequenza, 10))