import matplotlib.pyplot as plt

# Quadratic Model
a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(t):
    return a * (t**2) + b * t + c

hours = list(range(0, 25))  # 0 to 24
temps = [quadratic_weather_model(h) for h in hours]

# === WATERFALL MODE ===
plt.plot(hours, temps, 'r-', label="Waterfall (sequential)")

# === ITERATIVE MODE ===
iter_points = [0, 12, 24]
plt.plot(iter_points, [quadratic_weather_model(t) for t in iter_points],
         'go--', label="Iterative (stepwise)")

# === AGILE MODE ===
agile_points = [0, 6, 12, 18, 24]
plt.plot(agile_points, [quadratic_weather_model(t) for t in agile_points],
         'bs-', label="Agile (sprints)")

plt.title("Weather Modeling - Quadratic Solution")
plt.xlabel("Time (hours)")
plt.ylabel("Predicted Temperature (°C)")
plt.legend()
plt.grid(True)
plt.savefig("weather_models_graph.png")
plt.show()
