import numpy as np
import matplotlib.pyplot as plt

x = np.array([
    0.0634765625,
    0.0322265625,
    0.0166015625,
    0.0087890625,
    0.0048828125,
    1.0004882813,
    0.5004882813,
    0.2504882813,
    0.1254882813,
    0.06298828125,
    0.03173828125,
    0.01611328125,
    0.00830078125,
    1.0002441406,
    0.5002441406,
    0.2502441406
])

y_all_zero = np.array([
    5469.0784,
    5465.0157,
    5462.9363,
    5526.3085,
    5397.9853,
    5922.9869,
    5683.3434,
    5570.9046,
    5597.8291,
    5682.0822,
    5358.6253,
    5438.6342,
    5551.0387,
    6127.0176,
    5872.9773,
    5730.6419
])

y_1_to_10 = np.array([
    5634.9331,
    5604.8275,
    5597.1027,
    5629.9782,
    5593.8470,
    6058.0845,
    6110.2573,
    5791.8739,
    5602.3091,
    5653.6602,
    5736.5370,
    5600.0333,
    5775.3882,
    6517.8432,
    6159.5194,
    5789.1878
])

# Fit a polynomial (e.g., line, quadratic, etc.) to the data
deg = 1  # Degree of the polynomial. Change this depending on your needs.
fit_all_zero = np.polyfit(x, y_all_zero, deg)
fit_1_to_10 = np.polyfit(x, y_1_to_10, deg)

# Create a function based on the fit
f_all_zero = np.poly1d(fit_all_zero)
f_1_to_10 = np.poly1d(fit_1_to_10)

# Calculate R-squared
r_squared_all_zero = np.corrcoef(x, y_all_zero)[0, 1]**2
r_squared_1_to_10 = np.corrcoef(x, y_1_to_10)[0, 1]**2

# Generate x values for plotting the fit
x_fit = np.linspace(x.min(), x.max(), 500)

plt.scatter(x, y_all_zero, label='All zero')
plt.plot(x_fit, f_all_zero(x_fit), 'r-', label=f'Fit: All zero, R^2: {r_squared_all_zero:.3f}')

plt.scatter(x, y_1_to_10, label='1 to 10')
plt.plot(x_fit, f_1_to_10(x_fit), 'g-', label=f'Fit: 1 to 10, R^2: {r_squared_1_to_10:.3f}')

plt.legend()
plt.show()
