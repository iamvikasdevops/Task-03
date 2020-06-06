## file is not created by me ,creaed by someone
##
import os

acc = os.popen("cat /home/code/accuracy.txt")
acc1 = acc.read()
print(acc1)
acc2 = acc1.rstrip()
print(acc2)
acc3 = float(acc2)


if acc3<85:
    x = os.popen("cat /home/code/dlcode.py | grep model.add | wc -l")
    x1 = x.read()
    x2 = x1.rstrip()
    x3 = int(x2)
    print(x3)
    if x3==2:
        y = 'model.add(Dense(units=32, activation=\"relu\"))'
    elif x3==3:
        y = 'model.add(Dense(units=16, activation=\"relu\"))'
    elif x3==4:
        y = 'model.add(Dense(units=8, activation=\"relu\"))'
    else:
        print("MAAF KARDO")
        exit()
    os.system("sed -i '/softmax/ i {}' /code/dlcode.py".format(y))
    os.system("curl -u admin:redhat$ http://192.168.43.30:8080/view/Task-03%20MLOps/job/Launch_Container/build?token=vikash")
    acc = os.popen("cat /home/code/accuracy.txt")
    acc1 = acc.read()
    print(acc1)
    acc2 = acc1.rstrip()
    print(acc2)
    acc3 = float(acc2)
else:
    print("ACCURACY ABOVE 80")

