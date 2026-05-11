import numpy as np
from ControlModule import ControlModule


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

# Generamos la matriz P
P = ControlModule.generate_P(probs, n_states, n_actions)

print("Dimensiones de P:", P.shape)
print("Suma accion d desde S0:", np.sum(P[0, 0, :]))
print("Suma accion m desde S50:", np.sum(P[1, 50, :]))
print("Suma accion i desde S99:", np.sum(P[2, 99, :]))

# Generamos la matriz C para una demanda concreta
demand_t = 0.33
C = ControlModule.generate_C(demand_t, n_states, n_actions)

print("Dimensiones de C:", C.shape)

# Comprobaciones sencillas de costes
print("Coste de llegar a S33 con accion mantener:", C[1, 50, 33])
print("Coste de llegar a S51 con accion incrementar:", C[2, 50, 51])
print("Coste de llegar a S49 con accion decrementar:", C[0, 50, 49])

# Generamos la matriz R
R = ControlModule.generate_R(demand_t, n_states, n_actions)

print("Dimensiones de R:", R.shape)
print("Comprobacion R = -C:", R[1, 50, 33] == -C[1, 50, 33])

# Probamos una iteracion de control
current_state = 50

action = ControlModule.control_iteration(current_state,
                                         demand_t,
                                         P,
                                         n_states,
                                         n_actions,
                                         gamma)

print("Estado actual:", current_state)
print("Demanda actual:", demand_t)
print("Accion elegida:", action)

if action == 0:
    print("La accion elegida es: decrementar")
elif action == 1:
    print("La accion elegida es: mantener")
elif action == 2:
    print("La accion elegida es: incrementar")