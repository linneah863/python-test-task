from argparse import ArgumentError

def flag(N):
    half_flag = []
    half_flag.append('#'*(3*N+2))
    for i in range(N//2):
        half_flag.append('#'+' '*3*N+'#')
    for i in range(1, N//2+1):
        line = '#'+' '*(N+N//2-i)+'*'+'o'*(i-1)
        half_flag.append(line + line[::-1])
    for x in half_flag:
        print(x)
    half_flag.reverse()
    for x in half_flag:
        print(x)
N = input("Введите натуральное чётное число: ")

if N.isdigit() and int(N)%2==0:
    N = int(N)
    flag(N)
else:
    raise ArgumentError(None, "Не является натуральным чётным числом.")








# M = ['########', '#      #', '#  **  #']
# for x in M:
#     print(x)
# M.reverse()
# for x in M:
#     print(x)

# line2 = '#   '
# line3 = '#  *'
# m  = []
# m.append('#'*4*2)
# line2 = line2 + line2[::-1]
# m.append(line2)
# line3 = line3 + line3[::-1]
# m.append(line3)
# for x in m:
#     print(x)
# m.reverse()
# for x in m:
#     print(x)
