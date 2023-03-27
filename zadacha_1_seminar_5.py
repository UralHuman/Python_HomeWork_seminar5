# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     elif exponent % 2 == 0:
#         result = power(base, exponent/2)
#         return result * result
#     result = power(base, (exponent-1)/2)
#     return base * result * result
    
# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))

# print(f'{a} в степени {b} равно {power(a, b)}')

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        if exponent % 2 == 0:
            return power(base, exponent/2) * power(base, exponent/2)
        else:
            return power(base, (exponent-1)/2) * power(base, (exponent-1)/2) * base
        
a = int(input('Введите число А: '))
b = int(input('Введите число B: '))

print(f'{a} в степени {b} равно {power(a, b)}')