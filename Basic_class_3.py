# has_rice = True
# has_spoon =True

# if has_rice:
#     print('have rice')
#     if has_spoon:
#         print('have spoon')
#     else:
#         print('do not have spoon')
# else:
#     print('do not have rice')

#---------------------------------------------

# if has_rice == True and has_spoon == True:
#     print('ready to eat')
# else:
#     print('do not ready to eat')

#----------------------------------------------

# weak_up = True
# go_to_U = False

# if weak_up:
#     print('yes')
#     if go_to_U:
#         print('yes sir')
#     else:
#         print("i'm lazy")
# else:
#     print('sleep mode')

#---------------------------------

# what = True

# for i in range(1,7): 
#     if i == 3 :
#         print('starter pack')
#         if what == True:
#             print('true')
#         else:
#             print('false')
#         continue
       
#     print(i ,'hello')

#-------------------------------------------
# number = int(input('enter number1: ')) #ตัวเลขที่อยากได้
# time = int(input('enter number2: ')) #จำนวนรอบ

# for i in range(time):
#     num = int(input('num:'))
#     number -= num
#     print('เหลือ ',number)

#--------------------------------------------------

while True:
    x = input('number1: ')

    if x == '1': #แปลง 1 เป็น str
        print(x)
    else:
        print(x)
        break