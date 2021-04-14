# type 基本數據類型
#
# Number 數字
# int 整數(其他語言有分 short, int, long)
# float 浮點數(單精度 float, 雙精度 double, 不過 py 沒有分)
type(1) # <class 'int'>
type(1 + 1) # <class 'int'>
type(2 // 2) # <class 'int'> 雙 / 除法才會返回整數(1), 整除僅取整數位
type(1.1) # <class 'float'>
type(1.1111111111111111) # <class 'float'>
type(1 + 0.1) # <class 'float'>
type(1 + 1.0) # <class 'float'>
type(2 / 2) # <class 'float'> 除法返回是 float(1.0)
#
# 補充
# 10, 2, 8, 16 進制
# 10 滿 10 進 1, e.g. 0, 1, 2, ... 9, 10, 11, ...
# 2, e.g. 0, 1, 10, 11, 100, 101, ...
# 8, e.g. 0, 1, ..., 7, 10, ...
# 16, e.g. 0, 1, 2, ..., 9, A, B, C, D, E, F, ...
0b10 # 2 (0b 表示 2 進制)
0o10 # 8 (0o 表示 8 進制)
0x10 # 16 (0x 表示 16 進制)
bin(10) # '0b1010' X 進制轉 2 進制
oct(0b111) # '0o7' X 進制轉 8 進制
int(0b10) # 2 X 進制轉 10 進制
hex(888) # '0x378' X 進制轉 16 進制
#
# bool 布林(屬於數字分類的一種)
True
False
type(True) # <class 'bool'>
int(True) # 1
int(False) # 0
bool(1) # True (非空值(0, '', [], {}, None) 都是 True)
bool(0) # False
#
# complex 複數
36j # j 表示複數



# 變量
#