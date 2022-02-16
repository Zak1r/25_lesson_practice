# написать ф-ю, к-я будет принимать 1 параметр - размер ёлки 
# и будет выводить ёлку данного размера

# примерЖ
# draw_christmas_tree(5)
# Output:
# *
# **
# ***
# ****
# *****

# draw_christmas_tree(3)
# Output:
# *
# **
# ***


# def draw_christmas_tree(n):
#     z=n-1
#     x=1
#     for i in range(0,n):
#         for i in range(0,z):
#             print('',end='')
#         for i in range(0,x):
#             print('*',end='')
        
#         x=x+1
#         print()
# draw_christmas_tree(3)


# def draw_christmas_tree(size):
#     if type(size) == str or size < 3:
#         print('error')
#     else:
#         for i in range(1, size + 1):
#             print('*' * i)

# draw_christmas_tree(6)
# draw_christmas_tree(3)



#! Задача 2

# draw_rectanle(5,3)
#? output

# *****
# *****
# *****

# def draw_rectangle(width, height):
#     for i in range(height):
#         print('*' * width)

# draw_rectangle(10,2)


#! clear_text_from_uppercase('F3FNBJkjndjvlkjwFWIFJlkflkNF') -> 'iewjvnvnskjdvnsjkdvnsk'


# def clear_text_from_uppercase(text):
#     new_text = ''
#     for letter in text:
#         if letter.isupper():    pass
#         else:   new_text = new_text + letter
#     return new_text

# print(clear_text_from_uppercase('F3FNBJkjndjvlkjwFWIFJlkflkNF'))



# show_devisors(24) ->  1 2 3 4 6 8 12 24
# обнаружить целые числа которые делятся без остатка на параметр

def show_devisors(num):
    num1 = ''
    for i in range(num):
        if i % num == 0:    num1 = num1 + num
        else: pass
    return
print(show_devisors(24))