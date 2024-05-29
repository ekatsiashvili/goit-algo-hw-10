import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок для методу Монте-Карло
N = 10000

# Генерація випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Обчислення кількості точок під кривою
under_curve = y_random < f(x_random)
area_estimate = (b - a) * f(b) * np.sum(under_curve) / N

print("Оцінка інтеграла методом Монте-Карло:", area_estimate)

# Візуалізація результатів
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Випадкові точки
ax.scatter(x_random, y_random, s=1, color='blue', alpha=0.3, label='Random Points')
ax.scatter(x_random[under_curve], y_random[under_curve], s=1, color='green', alpha=0.3, label='Points Under Curve')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.legend()
plt.grid()
plt.show()
