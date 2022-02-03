from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import warnings
#unbounded_diff
# from DEbounded import run
from tkinter import messagebox

v = []
w = []
n = 0



def add():
   e = int(weight.get())
   w.append(e)
   e = int(value.get())
   v.append(e)


def addN():
    n = num.get()
    return n


def Wmax():
    maxWx = Mweight.get()
    return maxWx


def code():
    col= addN()
    col=int(col)
    n=col
    maxW=Wmax()
    maxW=int(maxW)
    row=50
    f = 0.8
    cr = 0.9
    mi=min(w)
    rand_pop = np.random.randint(0, maxW / mi, (row, col))
    rand_popTemp = np.random.randint(0, maxW / mi, (row, col))
    addZeros = np.zeros((row, 4))
    rand_pop = np.append(rand_pop, addZeros, axis=1)
    maxVal = 0
    bestChrom = []
    for itr in range(100):

        for i in range(row):

            sumWeight = sum(np.multiply(w, np.round(rand_pop[i, 0:col])))  # Total weight calculation
            rand_pop[i, col] = sumWeight
            sumValue = sum(np.multiply(v, np.round(rand_pop[i, 0:col])))
            if sumWeight > maxW:
                sumValue = 0
                rand_pop[i, col + 1] = sumValue
                continue

            rand_pop[i, col + 1] = sumValue
            if maxVal < sumValue:
                maxVal = sumValue
                # the chromosome with the best value
                bestChrom = rand_pop[i, 0:col]
                # Fitness(i) calculation

        for i in range(row):
            k1 = np.random.randint(0, row)
            k2 = np.random.randint(0, row)
            k3 = np.random.randint(0, row)

            while k1 == i:
                k1 = np.random.randint(0, row)
            while k2 == i or k2 == k1:
                k2 = np.random.randint(0, row)
            while k3 == i or k3 == k1 or k3 == k2:
                k3 = np.random.randint(0, row)
            trail = [0] * n
            u = [0] * n
            for j in range(n):
                z = rand_pop[k1, j] - rand_pop[k2, j]
                # trail.append(z)
                # print(z)

                z = np.round(z * f + rand_pop[k3, j])
                # trail.insert(j, np.round(trail[j] * f))
                # trail.insert(j, trail[j] + rand_pop[k3, j])

                h = trail.pop(j)
                trail.insert(j, z)

            rand1 = np.random.randint(0, col)
            rand2 = np.random.randint(0, col)
            while rand1 == rand2:
                rand2 = np.random.randint(0, col)

                h = u.pop(rand1)
                u.insert(rand1, trail[rand1])

                h = u.pop(rand2)
                u.insert(rand2, trail[rand2])

            for j in range(col):
                x = np.random.random((0, 1))
                if j == rand1 or j == rand2:
                    continue
                #warnings.simplefilter("ignore")
                if x > cr:

                    h = u.pop(j)
                    u.insert(j, rand_pop[j])

                else:

                    h = u.pop(j)
                    u.insert(j, trail[j])

            #print("before  ", u)
            # def bound(u):
            for j in range(col):
                if u[j] > maxW:

                    h = u.pop(j)
                    u.insert(j, 1)


                elif u[j] < 0:
                    if len(u) > 0:
                        h = u.pop(j)
                        u.insert(j, 0)

                # return u

            # u = bound(u)
            #print(u)

            def validate_genome(g):
                sum = 0
                for i in range(col):
                    if np.round(g[i]) == 1:
                        sum += w[i]
                        if sum > maxW:
                            return False

                return True

            b = validate_genome(u)

            def SumValue(v) -> int:
                sum = 0
                for i in range(col):
                    if np.round(u[i]) == 1:
                        sum += v[i]
                        # print(sum,"\n")
                return sum

            Value = 0
            if b:
                Value = int(SumValue(v))
                if Value > maxVal:
                    maxVal = Value
                    bestChrom = rand_pop[i, 0:col]
            else:
                Value = 0

            if rand_pop[i, col + 1] <= Value:
                rand_pop[i, 0:col] = np.reshape(u, (1, col))
                rand_pop[i, col + 1] = Value
                # rand_pop[i,col]=sumWeight
            # if maxVal<Value:
            # maxVal = Value
           # print("rand_pop  ", rand_pop)

            # the chromosome with the best value

   # print(maxVal, "  ", bestChrom)
    s1 = str(maxVal)
    s2 = str(bestChrom)
    s = str("Max Value: " + s1 + "  Best Chromosome:  " + s2 + " ")
    messagebox.showinfo("Solution", s)


def get_result():
    # not ready
    code()


screen = Tk()
screen.title('knapsack')
screen.geometry('800x500')
screen.config(bg='#D3D3D3')

screen.iconbitmap(r'knapsack.png')  # path of icon like D:/photos/Thief.ico
my_img = ImageTk.PhotoImage(Image.open(r'knapsack.png'))  # path of photo

my_label = Label(image=my_img)
my_label.pack()
addButton = Button(screen, text='Add Item', command=add)  # command is function that button will call
addButton.place(x=350, y=375)
bestkanp = Button(screen, text='best chromosome', command=get_result)
bestkanp.place(x=450, y=375)
addButton = Button(screen, text='enter number of items', command=addN)  # command is function that button will call
addButton.place(x=200, y=375)
# addButton.pack()
addButton = Button(screen, text='enter the max weight', command=Wmax)  # command is function that button will call
addButton.place(x=60, y=375)

#######################################################
l = Label(screen, text="weight", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=450, y=320)
weight = Entry(screen, width=15)
weight.place(x=450, y=350)
###########################################################
l = Label(screen, text="value", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=350, y=320)
value = Entry(screen, width=10)
value.place(x=350, y=350)
################################################

l = Label(screen, text="number of items", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=200, y=320)
num = Entry(screen, width=10)
num.place(x=200, y=350)
#######################################################

#######################################################
l = Label(screen, text="Max weight", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=70, y=320)
Mweight = Entry(screen, width=15)
Mweight.place(x=70, y=350)
screen.mainloop()

