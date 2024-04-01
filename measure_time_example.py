import time, random

def printAllTimeTable(time):
    for start in range(time, 10):
        for multiply in range(10):
            # print(" %d x %d = %d" % (start, multiply, start * multiply))
            pass

def printTimeTable(time):
    for i in range(10):
        # print("%d x %d = %d" % (time, i, time * i))
        pass

data = [random.randrange(1,10) for i in range(100000)]

startTime = time.time()

for num in data:
    printTimeTable(num)
print('elapsed time: %f' % (time.time() - startTime))

startTime = time.time()

for num in data:
    printAllTimeTable(num)
print('elapsed time: %f' % (time.time() - startTime))                                                                                                                 