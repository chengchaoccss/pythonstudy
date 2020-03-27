import multiprocessing as mp
import threading as td
import time

def job(q):
    # print("aaaa")
    res = 0
    for i in range(5000000):
        res+=i+i**2+i**3
    q.put(res)
# t1 = td.Thread(target =job,args=(1,2) )

def multicore():
    q=mp.Queue()
    p1 = mp.Process(target=job,args = (q,))
    p2 = mp.Process(target=job,args=(q,))
    p3 = mp.Process(target=job, args=(q,))
    p4 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p3.join()
    p4.join()
    res1 =q.get()
    res2 = q.get()
    res3 = q.get()
    res4 = q.get()
    print("multicore:",res1+res2+res3+res4)
def normal():
    # print("aaaa")
    res = 0
    for j in range(4):
        for i in range(5000000):
            res+=i+i**2+i**3
    print("normal:",res)

def multithread():
    q=mp.Queue()
    t1 = td.Thread(target=job,args = (q,))
    t2 = td.Thread(target=job,args=(q,))
    t3 = td.Thread(target=job,args=(q,))
    t4 = td.Thread(target=job, args=(q,))
    # t1.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    res1 =q.get()
    res2 = q.get()
    res3 =q.get()
    res4 = q.get()
    print("thread res:",res1+res2+res3+res4)


if __name__ == "__main__":
    st = time.time()
    normal()
    st1=time.time()
    print("normal time:",st1-st)

    multithread()
    st2 = time.time()
    print("multithread time:",st2-st1)

    multicore()
    st3 = time.time()
    print("multicore time:",st3-st2)