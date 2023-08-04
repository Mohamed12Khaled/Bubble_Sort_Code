l = []
x = int(input("enter the number of elements in the list"))
for i in range(x):
    y = int(input("enter the number"))
    l.append(y)


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                print(l)
bubble_sort(l)
#________________________________________________________________________________________
list = []
x = int(input("enter the number of elements in the list"))
for i in range(x):
    y = int(input("enter the number"))
    list.append(y)


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list)
bubble_sort(l)