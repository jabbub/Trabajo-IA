# Import required dependencies
import numpy as np
import mdptoolbox

class ControlModule:
    def __init__(self):
        """ Dummy constructor to use the Python Class as a namespace """
        pass

    @staticmethod
    def generate_P(probs: np.ndarray, n_states: np.int32) -> np.ndarray:
        """
        Genera la matriz de transición P con forma (n_actions, n_states, n_states).
        P[a][s][s'] = probabilidad de pasar al estado s' desde s tomando la acción a.

        Las acciones y sus deltas posibles son:
        0 - decrease: [-2, -1,  0]
        1 - mantain: [-1,  0, +1]
        2 - increase: [ 0, +1, +2]

        En los extremos (s=0 y s=99) las transiciones fuera de rango
        se absorben en el estado frontera correspondiente.
        """
        n_actions = 3
        acciones = [
            [-2, -1, 0],  # Acción 0: Decrease (d)
            [-1,  0, 1],  # Acción 1: Mantain (m)
            [ 0,  1, 2]   # Acción 2: Increase (i)
        ]

        P = np.zeros((n_actions, n_states, n_states), dtype=np.float64)
        for a in range(n_actions):
            for s in range(n_states):
                for prob, delta in zip(probs[a], acciones[a]):
                    s_next = np.clip(s + delta, 0, n_states - 1) # Estado destino con absorción en los extremos
                    P[a][s][s_next] += prob # Acumular la probabilidad para el estado siguiente s_next
        return P



    @staticmethod
    def generate_R(demand_t: np.float64, n_states: np.int32) -> np.ndarray:
        """
        Genera la matriz de costes/recompensas R con forma (n_actions, n_states, n_states).
        R[a][s][s'] = recompensa (negativo del coste) de transicionar de s a s' con acción a,
        dado el punto de demanda actual demand_t.

        Coste base:    |demand_t - pow(s')|         donde pow(s') = s' * 0.01
        Penalización:  x2 si la acción se aleja del objetivo:
                - increase (a=2) cuando pow(s') > demand_t
                - decrease (a=0) cuando pow(s') < demand_t

        Se devuelve el negativo del coste porque pymdptoolbox maximiza recompensa.
        """
        n_actions = 3
        R = np.zeros((n_actions, n_states, n_states), dtype=np.float64)

        for s_prime in range(n_states):
            # Potencia normalizada (límite inferior del intervalo)
            pow_s_prime = s_prime * 0.01

            # Distancia base entre la demanda actual y el estado destino
            base_cost = abs(demand_t - pow_s_prime)

            for a in range(n_actions):
                # Penalización x2 si la acción contradice el objetivo
                if a == 0 and pow_s_prime < demand_t:
                    # decrease aleja si el destino ya está por debajo de la demanda
                    cost = 2.0 * base_cost
                elif a == 2 and pow_s_prime > demand_t:
                    # increase aleja si el destino ya está por encima de la demanda
                    cost = 2.0 * base_cost
                else:
                    cost = base_cost

                # Aplicar el mismo coste a todas los s de origen
                # y negar para convertir coste en recompensa
                R[a, :, s_prime] = -cost

        return R

    @staticmethod
    def control_iteration() -> np.int32:
        """ Function that computes one control-iteration """
        ### TO BE COMPLETED BY THE STUDENTS ###
        ...

    @staticmethod
    def control_loop(demand: np.ndarray, 
                     probs: np.ndarray,
                     n_states: np.int32, 
                     n_actions: np.int32,
                     gamma: np.float64) -> np.ndarray:
        """ Function that computes all the required iterations (control-loop) to satisfy the power demand """
        ### TO BE COMPLETED BY THE STUDENTS ###

        ### DUMMY BEHAVIOUR TO PREVENT CRASHING (MUST BE DELETED AFTER THE FULL IMPLEMENTATION) ###
        return np.zeros_like(a=demand, dtype=np.float64)
        ### ###
