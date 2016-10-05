# -*- encoding: utf-8 -*-
import random
import math

citysX = [16,17,12,10,30,40,10,11,29,55,160,170,120,100,99,78,100,111,64,123]
citysY = [3,39,31,60,29,4,38,40,22,45,35,88,31,60,55,87,38,40,22,123]
first=second=best=0
citynum=citynum1=citynum2=citynum3=citynum4=citynum5= []
index=2

def initsequence():
    '''初始化'''
    global citynum
    citynum = [member for member in range(20)]
    random.shuffle(citynum)

def choosepoint():
    '''选择断点'''
    global first
    global second
    first = random.randint(1, 18)
    second = random.randint(1, 18)
    while abs(first-second)<2:
        second = random.randint(1, 18)
    if first>second:
        temp=second
        second=first
        first=temp

def disorder():
    '''创建临近解空间'''
    global first
    global second
    global citynum1
    global citynum2
    global citynum3
    global citynum4
    global citynum5
    ran1 = citynum[:first]
    ran2 = citynum[first:second]
    ran3 = citynum[second:]
    citynum1 = ran1+ran3+ran2
    citynum2 = ran2+ran1+ran3
    citynum3 = ran2+ran3+ran1
    citynum4 = ran3+ran1+ran2
    citynum5 = ran3+ran2+ran1

def distance(num):
    '''评估'''
    distance = 0.0
    #print(num)
    for i in range(19):
        distance += math.sqrt((citysX[num[i]] - citysX[num[i+1]]) ** 2 + (citysY[num[i]] - citysY[num[i+1]]) ** 2)
    return distance

def run():
    '''每次选出最好的'''
    global citynum
    global best
    global index
    choosepoint()
    disorder()
    a = distance(citynum)
    b = distance(citynum1)
    c = distance(citynum2)
    d = distance(citynum3)
    e = distance(citynum4)
    f = distance(citynum5)
    sequence=[a,b,c,d,e,f]
    sequence.sort()
    best=sequence[0]
    if best==a:
        citynum=citynum
        pass
    elif best==b:
        citynum=citynum1
        pass
    elif best==c:
        citynum=citynum2
        pass
    elif best==d:
        citynum=citynum3
        pass
    elif best==e:
        citynum=citynum4
        pass
    elif best==f:
        citynum=citynum5
    print(index,float('%.5f'% best),citynum)
    index+=1

def main():
    a=int(input("please define the number of iteration:"))
    initsequence()
    while a > 0:
        run()
        a-=1

main()




