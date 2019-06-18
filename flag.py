from argparse import ArgumentError

def flag(N):
    half_flag = []
    half_flag.append('#'*(3*N+2))
    for i in range(N//2):
        half_flag.append('#'+' '*3*N+'#')
    for i in range(1, N//2+1):
        line = '#'+' '*(N+N//2-i)+'*'+'o'*(i-1)
        half_flag.append(line + line[::-1])
    flag_string = '\n'.join(half_flag)
    half_flag.reverse()
    flag_string = flag_string + '\n' + '\n'.join(half_flag)
    return flag_string


N = input("Введите натуральное чётное число: ")

if N.isdigit() and int(N)%2==0:
    N = int(N)
    print(flag(N))
else:
    raise ArgumentError(None, "Не является натуральным чётным числом.")
