
import threading
import pandas
import time

def fun1():
    
    datafarame = pandas.read_csv('D:\VScode\OS project\dataset.csv')
    max = datafarame.loc[datafarame['Global_Sales'].idxmax()]
    print("Max value : \n")
    print(max)


def fun2():
    
    datafarame = pandas.read_csv('D:\VScode\OS project\dataset.csv')
    min = datafarame.loc[datafarame['Global_Sales'].idxmin()]
    print("Min value : \n")
    print(min)


def main():
    
    # The current time when the code below executes
    start = time.time()
    thread1 = threading.Thread(target = fun1)
    thread2 = threading.Thread(target = fun2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # The current time when the code below executes
    end = time.time()
    
    print("============================================================")
    print("time : ",end - start)
          
        
if __name__ == '__main__':
    main()

