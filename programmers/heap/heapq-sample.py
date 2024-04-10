from heapq import heappush, heappop

sample = [3,0,1,8,7,2,5,4,6,9]

def heapSort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]


