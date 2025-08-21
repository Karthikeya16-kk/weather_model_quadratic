import matplotlib.pyplot as plt

# Quadratic Model
a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(t):
    return a * (t**2) + b * t + c

hours = list(range(0, 25))  # 0 to 24

# ===== WATERFALL MODE =====
temps_waterfall = [quadratic_weather_model(h) for h in hours]
plt.plot(hours, temps_waterfall, 'r-')
plt.title("Weather Modeling - Waterfall Model")
plt.xlabel("Time (hours)")
plt.ylabel("Predicted Temperature (°C)")
plt.grid(True)
plt.savefig("graph_waterfall.png")
plt.close()

# ===== ITERATIVE MODE =====
iter_points = [0, 12, 24]
temps_iterative = [quadratic_weather_model(t) for t in iter_points]
plt.plot(iter_points, temps_iterative, 'go--')
plt.title("Weather Modeling - Iterative Model")
plt.xlabel("Time (hours)")
plt.ylabel("Predicted Temperature (°C)")
plt.grid(True)
plt.savefig("graph_iterative.png")
plt.close()

# ===== AGILE MODE =====
agile_points = [0, 6, 12, 18, 24]
temps_agile = [quadratic_weather_model(t) for t in agile_points]
plt.plot(agile_points, temps_agile, 'bs-')
plt.title("Weather Modeling - Agile Model")
plt.xlabel("Time (hours)")
plt.ylabel("Predicted Temperature (°C)")
plt.grid(True)
plt.savefig("graph_agile.png")
plt.close()

print("✅ Graphs saved: graph_waterfall.png, graph_iterative.png, graph_agile.png")
