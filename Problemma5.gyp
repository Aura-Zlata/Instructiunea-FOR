"""
Utilizînd ciclul FOR elaboraţi un program care să calculeze suma numerelor de la 1 la n, care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură.
"""
n=52
s=1
p=1
end=n
for i in range(1,52):
    if i<26:
        s+=i
    else:
        p%=3
        p%=5
print("suma este",s)
print("catul este",p)