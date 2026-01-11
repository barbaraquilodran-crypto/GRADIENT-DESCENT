def derivada(f, x, h=0.01):
    gradiente = (f(x + h)- f(x))/h
    return gradiente
