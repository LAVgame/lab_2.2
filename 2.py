
print("Введитие А x1 координату:")
x1 = int(input())

print("Введитие А y1 координату:")
y1 = int(input())

print("Введитие B x2 координату:")
x2 = int(input())

print("Введитие B y2 координату:")
y2 = int(input())
if  abs(x1) > abs(x2):
    if abs(y1) > abs(y2):
        print("А дальше")
    else:
        print("B дальше")
else:
    print("B дальше")