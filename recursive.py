import time

sour = [] 
dest = [] 
buff = [] 

def fill_source(num):
    i = 1
    while(i <= num):
        try:
            dest.pop()
        except IndexError:
            pass
        sour.append(i)
        i += 1

def print_towers():
    print('Sour: ' + str(sour))
    print('Buff: ' + str(buff))
    print('Dest: ' + str(dest))

def move(sour, dest):
    if len(sour) != 0:
        dest.append(sour.pop())

def solve_towers(n, sour, dest, buff):
    if n == 0:
        return

    solve_towers(n - 1, sour, buff, dest)

    move(sour, dest)
    # print_towers()

    solve_towers(n - 1, buff, dest, sour)

def Hanoi(num):
    fill_source(num)
    # print_towers()
    solve_towers(num, sour, dest, buff)
    # print_towers()

def measure_time():
    i = 2
    while(i < 21):
        start = time.time()
        Hanoi(i)
        end = time.time() - start
        print("Recursion no. " + str(i) + " time: " + str(end))
        i += 1

measure_time()