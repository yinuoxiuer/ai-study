# 2026年01月25日08时01分36秒
# xxx@qq.com
import random
import time
import sys
sys.setrecursionlimit(100000000)
print(hash('a'))
class Sort:
    def __init__(self,n):
        self.len=n
        self.arr=[0]*n
    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0,100000)
    def quick_sort(self,left,right):
        pivot=self.partition(left,right)
        if left<pivot-1:
            self.quick_sort(left,pivot-1)
        if pivot+1<right:
            self.quick_sort(pivot+1,right)
    def partition(self,left,right):
        random_pos=random.randint(left,right)
        self.arr[right],self.arr[random_pos]=self.arr[random_pos],self.arr[right]
        #这两步可以解决基本有序的最坏情况
        k=left
        for i in range(left,right):
            if self.arr[i]<self.arr[right]:
                self.arr[i],self.arr[k]=self.arr[k],self.arr[i]
                k+=1
        self.arr[k],self.arr[right]=self.arr[right],self.arr[k]
        return k
    def adjust_max_heap(self,pos,arr_len):
        dad=pos
        son1=2*pos+1
        son2=2*pos+2
        if son1<arr_len:
            if son2<arr_len:
                if self.arr[son1]>self.arr[son2] and self.arr[son1]>self.arr[dad]:
                    self.arr[son1],self.arr[dad]=self.arr[dad],self.arr[son1]
                    self.adjust_max_heap(son1,arr_len)
                elif self.arr[son2]>self.arr[dad]:
                    self.arr[son2],self.arr[dad]=self.arr[dad],self.arr[son2]
                    self.adjust_max_heap(son2,arr_len)
            elif self.arr[son1]>self.arr[dad]:
                self.arr[son1],self.arr[dad]=self.arr[dad],self.arr[son1]
                self.adjust_max_heap(son1, arr_len)
    def heap_sort(self):
        for parent in range((self.len-1)//2,-1,-1):
            self.adjust_max_heap(parent,self.len)
        self.arr[0],self.arr[self.len-1]=self.arr[self.len-1],self.arr[0]
        for k in range(self.len-1,0,-1):
            self.adjust_max_heap(0,k)
            self.arr[0],self.arr[k-1]=self.arr[k-1],self.arr[0]
    def time_test(self, func, *args):
        start=time.time()
        func(*args)
        end=time.time()
        print(end-start)
if __name__ == '__main__':
    my_sort=Sort(100000)
    my_sort.random_data()
    # print(my_sort.arr)
    # my_sort.quick_sort(0,my_sort.len-1)
    # print(my_sort.arr)
    # my_sort.heap_sort()
    # print(my_sort.arr)
    my_sort.time_test(my_sort.quick_sort,0,my_sort.len-1)

