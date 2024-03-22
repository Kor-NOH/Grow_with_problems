import sys

a = 1

while a != 0:
    gather_check = 0
    gather_cnt, consonant_cnt = 0, 0
    cnt_over = 0
    str_over = 0
    past = ''

    user_input = sys.stdin.readline().strip()
    if user_input == 'end':
        break
    else:
        str_input = list(str(user_input))
        for gather in str_input:
            if gather == 'a' or gather == 'e' or gather == 'i' or gather == 'o' or gather == 'u':
                gather_check += 1


        if gather_check == 0:
            sys.stdout.write('<')
            sys.stdout.write(user_input)
            sys.stdout.write('> is not acceptable.'+'\n')

        else:
            for cnt_check in str_input:
                if cnt_check == 'a' or cnt_check == 'e' or cnt_check == 'i' or cnt_check == 'o' or cnt_check == 'u':
                    gather_cnt += 1
                    consonant_cnt = 0
                else:
                    consonant_cnt += 1
                    gather_cnt = 0

                if gather_cnt == 3 or consonant_cnt == 3:
                    cnt_over = 1

            if cnt_over == 1:
                sys.stdout.write('<')
                sys.stdout.write(user_input)
                sys.stdout.write('> is not acceptable.' + '\n')

            else:
                for i in str_input:
                    if i == past:
                        if i != 'e' and i != 'o':
                            str_over = 1

                    past = i

                if str_over == 1:
                    sys.stdout.write('<')
                    sys.stdout.write(user_input)
                    sys.stdout.write('> is not acceptable.' + '\n')

                else:
                    sys.stdout.write('<')
                    sys.stdout.write(user_input)
                    sys.stdout.write('> is acceptable.' + '\n')
