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

def move(first, second):
    if len(first) == 0 or len(second) == 0:
        if len(first) == 0:
            first.append(second.pop())
        elif len(second) == 0:
            second.append(first.pop())
    else:
        if first[-1] > second[-1]:
            second.append(first.pop())
        else:
            first.append(second.pop())

def print_towers():
    print('Sour: ' + str(sour))
    print('Buff: ' + str(buff))
    print('Dest: ' + str(dest) + "\n")

def solve_iterative(num, sour, dest, buff):
    i = 1
    while(len(sour) != 0 or len(buff) != 0):
        if i%3 == 1:
            move(sour, dest) if num%2 == 1 else move(sour, buff)
        if i%3 == 2:
            move(sour, buff) if num%2 == 1 else move(sour, dest)
        if i%3 == 0:
            move(buff, dest)
        # print_towers()
        i += 1

def Hanoi(num):
    fill_source(num)
    # print_towers()
    solve_iterative(num, sour, dest, buff)
    # print_towers()
    
def measure_time():
    i = 2
    while(i < 21):
        start = time.time()
        Hanoi(i)
        end = time.time() - start
        print("Iteration no. " + str(i) + " time: " + str(end))
        i += 1

measure_time()