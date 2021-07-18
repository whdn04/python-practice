from random import *
import random


count = 0
for x in range(1, 51):
    time = random.randint(1, 51)
    if 5 <= time <= 15:
        print(f"[o] {x}번째 손님 (소요시간 : {time}분)")
        count += 1
    else:
        print(f"[] {x}번째 손님 (소요시간 : {time}분)")


print(count)
