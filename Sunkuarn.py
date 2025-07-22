while True:
    m = int(input('distance: '))

    if m >= 5 and m <= 50:
        print('10 Bath')
    elif m >= 51 and m <= 100:
        print('15 Bath')
    elif m >= 101 and m <= 300:
        print('25 Bath')
    elif m >= 301 and m <= 500:
        print('35 Bath')
    elif m >= 500:
        print('45 Bath')
    else:
        print('ยังไม่ถึงระยะทางขั้นต่ำ')


