import math

print("Первое задание, первый пункт")
a = int(input())
print("s = ", a * a)
print("Первое задание, второй пункт")
S = 32
R =  math.sqrt(S/math.pi)
print(f"L = {2 * math.pi * R:.2f}, D = {2 * R:.2f}")
print("Первое задание, третий пункт")
hmmss = int(input())
h = hmmss // 3600
ost = hmmss % 3600
mm = ost // 60
ss = ost % 60
disp_h = h % 12
if disp_h == 0:
    disp_h = 12

print(f"{disp_h}:{mm:02d}:{ss:02d}")