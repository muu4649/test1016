import numpy as np
import pandas as pd

def calc(a):
    for i in range(1,11):
        a=a*i
    return a

def main():
    a=28
    b=calc(a)
    print(b)


if __name__=='__main__':
     main()
