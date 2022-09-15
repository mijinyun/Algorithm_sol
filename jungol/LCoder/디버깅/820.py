import time
 
now = time.localtime()
a = 0
a = now.tm_year-1900          # ----------------------- ①
a += now.tm_mon-1              # ----------------------- ②
a += now.tm_mday
print(122, 9, 15)                   # ----------------------- ③ 
#위 문장에서 출력될 값들을 각각 ① ② ③위치에서의 a의 값으로 바꾸어 준다.