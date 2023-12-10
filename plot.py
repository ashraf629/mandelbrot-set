import matplotlib.pyplot as plt

def mandelbrot(c,max_iter):
    z=0
    for i in range(max_iter+1):
        z=z*z+c
        if not abs(z) < 2: return False
    return True

xx = []

yy = []

def mandelplot(x_min,x_max,y_rad,stepsize,max_iter):
    r = x_max - x_min
    x_bits = int(r/stepsize)
    y_bits = int(2*y_rad/stepsize)
    for i in range(x_bits):
        for j in range(y_bits):
            x=x_min+i*stepsize
            y=-1*y_rad+j*stepsize
            if mandelbrot(complex(x,y),max_iter):
                xx.append(x)
                yy.append(y)

mandelplot(-2,0.5,1.1,0.05,3000)

fig, ax = plt.subplots()
ax.scatter(xx, yy ,color='black' ,marker='o', s=(72./fig.dpi)**2)
plt.savefig('mandelbrot.pdf')
