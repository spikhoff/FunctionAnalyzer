import numpy as np
from scipy.integrate import quad

# Defineerime funktsiooni
def f(x):
    return x**2

# Määrame integreerimise piirid
a, b = 0, 4

# Integraali arvutamine
integral_result, _ = quad(f, a, b)

# Arvutame keskmise väärtuse
keskmine_väärtus = integral_result / (b - a)

# Arvutame funktsiooni globaalse maksimumi vahemikus
x_values = np.linspace(a, b, 400)
y_values = f(x_values)
global_max = np.max(y_values)

print(f"Integraali väärtus vahemikus {a} kuni {b}: {integral_result}")
print(f"Funktsiooni keskmine väärtus vahemikus {a} kuni {b}: {keskmine_väärtus}")
print(f"Funktsiooni globaalne maksimum vahemikus {a} kuni {b}: {global_max}")
