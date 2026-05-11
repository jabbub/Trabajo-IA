import numpy as np
from ControlModule import ControlModule


np.random.seed(123)

# Probabilidades de ejemplo, con el mismo orden que en los JSON:
# decrease, maintain, increase
probs = np.array([
    [0.55, 0.20, 0.25],
    [0.95, 0.025, 0.025],
    [0.65, 0.25, 0.10]
], dtype=np.float64)

n_states = 100
n_actions = 3
gamma = 0.9

# Demanda pequeña de prueba
demand = np.array([0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45], dtype=np.float64)

response = ControlModule.control_loop(demand,
                                      probs,
                                      n_states,
                                      n_actions,
                                      gamma)

print("Demanda:", demand)
print("Respuesta:", response)
print("Dimensiones de la respuesta:", response.shape)
print("Valor minimo de la respuesta:", np.min(response))
print("Valor maximo de la respuesta:", np.max(response))

if response.shape == demand.shape:
    print("La respuesta tiene la misma longitud que la demanda")

if np.min(response) >= 0 and np.max(response) <= 1:
    print("La respuesta esta dentro del intervalo [0, 1]")
    