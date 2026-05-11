    import json
import numpy as np
from Reactor import Reactor


with open("Reactors/R0.json", "r", encoding="utf-8") as file:
    data = json.load(file)

reactor = Reactor(model=data["model"],
                  effective_section=float(data["effective_section"]),
                  neutron_flux=float(data["neutron_flux"]),
                  core_volume=float(data["core_volume"]),
                  fision_energy=float(data["fision_energy"]),
                  probabilities=dict(data["probabilities"]))

print(reactor)
print("Potencia maxima:", reactor.max_power)
print("Constante k:", reactor.k)

print("Potencia con barras al 0%:", reactor.compute_power(0.0))
print("Potencia con barras al 50%:", reactor.compute_power(0.5))
print("Potencia con barras al 100%:", reactor.compute_power(1.0))

print("Insercion para potencia 1.0:", reactor.compute_control_bars_insertion(1.0))
print("Insercion para potencia 0.5:", reactor.compute_control_bars_insertion(0.5))
print("Insercion para potencia 0.0:", reactor.compute_control_bars_insertion(0.0))

if reactor.max_power > 0:
    print("Potencia maxima correcta")

if reactor.k > 0:
    print("Constante k correcta")

if 0 <= reactor.compute_power(0.5) <= 1:
    print("Potencia normalizada correcta")

if 0 <= reactor.compute_control_bars_insertion(0.5) <= 1:
    print("Insercion de barras correcta")
    