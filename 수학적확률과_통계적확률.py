from matplotlib import pyplot as plt
import random
def graph(시행_횟수):
    주사위_면=6
    spots_on_a_die=[]
    for i in range(0, 주사위_면):
        spots_on_a_die.append(i+1)
    li=[]
    num=0
    while num<시행_횟수:
        li.append(random.choice(spots_on_a_die))
        num=num+1
    data=[]
    for i in range(0, 주사위_면):
        횟수=li.count(i+1)
        data.append(횟수/시행_횟수)
    plt.plot(spots_on_a_die, data, color="red")
    plt.bar(spots_on_a_die, data, color="blue")
    plt.ylabel("probability("+str(시행_횟수)+" trials)")
    plt.xlabel("spots on a die")
    plt.show()
while True:
    how=int(input('몇 번 던질까요? '))
    graph(how)