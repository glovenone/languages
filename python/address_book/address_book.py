import os
import pickle
if os.path.exists('person.data') == False:
    f = open('person.data', 'wb')
    temp = {'total' : 0}
    pickle.dump(temp, f)
    f.close()
else:
    pass
#add():
def add():
    f = open('person.data', 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    name = raw_input("tell me the name you wanna add:")
    for key in a.keys():
        b += 1
        if key == name and b <= a['total']+1:
            print("the person you wanna add is already here!")
            break
        if b == a['total']+1 and key != name:
            number = input("tell me the number:")
            information = {name:number}
            a['total'] += 1
            a.update(information)
            f = open('person.data', 'wb')
            pickle.dump(a, f)
            f.close()
            print("Worked!")
            break
#show():
def show():
    f = open('person.data', 'rb')
    a = pickle.load(f)
    print("there are/is totally {} person(s)." .format(a['total']))
    for key in a.keys():
        if key != 'total':
            print('{' '}:{' '}' .format(key,a[key]))
    f.close()
#exit():
def exit():
    exec("quit()")
#search():
def search(name):
    f = open('person.data', 'rb')
    a = pickle.load(f)
    b = 0
    for key in a.keys():
        b += 1
        if key == name and b <= a['total']+1:
            print("{}'number is : {}" .format(name,a[key]))
            break
        if b == a['total']+1 and key != name:
            print("the person you search is not here!")
            break
    f.close()
#deleate()
def deleate(name):
    f = open('person.data', 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    for key in a.keys():
        b += 1
        if key == name and b <= a['total']+1:
            a.pop(name)
            a['total'] -= 1
            f = open('person.data', 'wb')
            pickle.dumps(a, f)
            f.close()
            print("Deleated!")
            break
        if b == a['total']+1 and key != name:
            print("the person is not here")
            break
#change():
def change():
    x = raw_input("tell me the name who you wanna edit:")
    f = open('person.data', 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    for key in a.keys():
        b += 1
        if key == x and b <= a['total']+1:
            y = input("the number after edit:")
            a[key] = y
            f = open('person.data','wb')
            pickle.dump(a, f)
            f.close()
            print("Worked!")
            break
        if key != x and b == a['total']+1:
            print("the person is not here!")
            break
#destop:
def point():
    print( "*************")
    print("details:     0")
    print("peoples:     1")
    print("search:      2")
    print("add:         3")
    print("deleate:     4")      
    print("edit:        5")
    print("exit:        6")
    print("**************")
point()
while True:
    x = input("input your choice~\n")
    if x == 3:
        add()
        continue
    if x == 1:
        show()
        continue
    if x == 6:
        exit()
        continue
    if x == 2:
        name = raw_input("input the name you wanna search:")
        search(name)
        continue
    if x == 4:
        name = raw_input("input the name you wanna deleate:")
        deleate(name)
        continue
    if x == 5:
        change()
        continue
    if x == 0:
        point()
    else:
        print("the choice you input is not exit!")
        continue
