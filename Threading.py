import threading
import time

listThread = []

def func():
    print('ran')
    time.sleep(0.8)
    print("done")
    time.sleep(1)
    print("now done")

def count (n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)

def count2 (n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.02)

def count2 (n):
    for i in range(1,n+1):
        print(i)
        listThread.append(i)   
        
# main thread + x thread
#thread object

x = threading.Thread(target=func)
x.start()
print(threading.activeCount())
time.sleep(0.9)
print("wait")
'''
output:
ran
2
done
wait
now done
'''


for _ in range(2): # starting 2 threads
    th = threading.Thread(target=count, args=(10,)) # count to 100
    th.start()
print("Done for the  number")
'''
output :
1
1
Done
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10

output 2(the 1st thread goes brrr):
1
1
Done for the  number
2
2
3
3
4
5
5
6
6
7
8
7
9
8
9
10
10
'''
th1 = threading.Thread(target=count, args=(10,)) # count to 100
th1.start()

th2 = threading.Thread(target=count2, args=(10,)) # count to 100
th2.start()
print("Done")
'''
output (rdm output lol) :
1
1
Done
2
2
3
4
3
5
6
4
7
8
5
9
6
10
7
8
9
10
'''
time.sleep(1)

print(listThread)
'''
output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''