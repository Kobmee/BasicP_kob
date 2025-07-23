HP_monster = 100
weapon1,weapon2,weapon3 = 10,20,30


while True:
    fi_nf = int(input('fight? : '))

    if fi_nf == 1:
        hit = int(input('How many round do you hit: '))
    for fi_nf in range(hit):
            choose = input('choose_w: ')
            HP_monster -= choose
            print(HP_monster)

        