import numpy as np
import matplotlib.pyplot as plt

n_values = [100, 1000, 5000, 10000, 50000, 100000]  

# Интеграл I1
def func_I1(x):
    return np.exp(-x) * np.sin(x)**5

# Интеграл I2
def func_I2(x, y):
    return (x**3 + 3*x*y) / np.exp(y)

def monte_carlo_I1(n):
    a = 1  
    samples = np.random.exponential(1.0, n) + a  
    samples = samples[samples > a]  
    values = func_I1(samples) / np.exp(samples - a)  
    return np.mean(values)

def monte_carlo_I2(n):
    samples_x = np.random.uniform(-1, 1, n)
    samples_y = np.random.uniform(-1, 1, n)
    inside_region = np.abs(samples_x) + np.abs(samples_y) < 1
    values = func_I2(samples_x[inside_region], samples_y[inside_region])
    area = 2 * 2 * np.sum(inside_region) / n  
    return np.mean(values) * area

results_I1 = []
results_I2 = []

for n in n_values:
    I1_estimate = monte_carlo_I1(n)
    I2_estimate = monte_carlo_I2(n)
    results_I1.append(I1_estimate)
    results_I2.append(I2_estimate)

plt.figure(figsize=(12, 6))

# График для I1
plt.subplot(1, 2, 1)
plt.plot(n_values, results_I1, 'o-', label='$I_1$ (Monte-Carlo)')
plt.xscale('log')
plt.xlabel("Число итераций n")
plt.ylabel("Приближенное значение интеграла")
plt.title("Метод Монте-Карло для $I_1$")
plt.legend()
plt.grid()

# График для I2
plt.subplot(1, 2, 2)
plt.plot(n_values, results_I2, 'o-', label='$I_2$ (Monte-Carlo)')
plt.xscale('log')
plt.xlabel("Число итераций n")
plt.ylabel("Приближенное значение интеграла")
plt.title("Метод Монте-Карло для $I_2$")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
