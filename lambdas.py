import matplotlib.pyplot as plt

def func(a,b,c):
    return lambda x: a*x**2 + b*x + c

funcao = func(-.1,20,3)
func_plt = []
for n in range(200):
   func_plt.append(funcao(n))
plt.plot(func_plt)
plt.show()

# É utilizado o lambda para definir uma função anônima
# que será utilizada posteriormente.
