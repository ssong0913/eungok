import func_kwargs
from func_args import 함수
from func_kwargs import *

from func_kwargs import name_hello_함수 as nh
# from(큰 범위) func_kwargs에서 => import name_hello_함수 함수를 가져와 => as nh 로 이름변경
import numpy as np
# pip install numpy

# func_kwargs.name_hello_함수(a="kim", b="park", c="lee")
data = 함수(1,5,6,4,3,100)
print(data)
# name_hello_함수(a="kim", b="park", c="lee")
nh(a="kim", b="park", c="lee")

#상위경로 import
# ↓ 상위 폴더의 위치를 현재와 동일하게 만든다. 
import sys, os
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import hello

file_path = "C:\apps\test"
sys.path.append(file_path)


list_1 = [1,2,3,4,5]
list_2 = [2,5,3,2,10]
a = np.array(list_1)
b = np.array(list_2)
# numpy array 를 이용하여 배열로 바꿈

print(list_1 + list_2)
print(a+b)
