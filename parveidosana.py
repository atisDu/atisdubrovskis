#int pārveidošana par str
a = 5
b = 7
print("skaitlis ir",a + b)
print("Teksts",str(a)+str(b))

#izveidot 2 str tipa mainīgos 1."123" 2."456"
#pārveidot šōs mainīgos par int tipa
#noteikt datu tipu

skaitli0 = "123"
skaitli1 = "456"

skaitli0_int = int(skaitli0)
skaitli1_int = int(skaitli1)

print(type(skaitli0_int),type(skaitli1_int))

r = "123"
o = "456"
g = int(r)
q = int(o)
print(g+q,type(q+g))