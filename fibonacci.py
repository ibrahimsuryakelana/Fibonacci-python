d1=0
d2=1

n = int(input("Masukan batas deret : "))

for i in range (n):
    print(d1, end=' ')
    d3 = d2 + d1
    d1 = d2
    d2 = d3
