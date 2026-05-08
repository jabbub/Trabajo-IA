# Import required dependencies
import numpy as np
import mdptoolbox

class ControlModule:
    def __init__(self):
        """ Dummy constructor to use the Python Class as a namespace """
        pass

    @staticmethod
    def generate_P(probs: np.ndarray, n_estados: np.int32) -> np.ndarray:
        """
        Genera la matriz de transición P con forma (n_acciones, n_estados, n_estados).
        P[a][s][s'] = probabilidad de pasar al estado s' desde s tomando la acción a.

        Las acciones y sus deltas posibles son:
        0 - decrementar: [-2, -1,  0]
        1 - mantener: [-1,  0, +1]
        2 - inrementar: [ 0, +1, +2]

        En los extremos (s=0 y s=99) las transiciones fuera de rango
        se absorben en el estado frontera correspondiente.
        """
        n_acciones = 3
        acciones = [
            [-2, -1, 0],  # Acción 0: Decrementar (d)
            [-1,  0, 1],  # Acción 1: Mantener (m)
            [ 0,  1, 2]   # Acción 2: Incrementar (i)
        ]

        P = np.zeros((n_acciones, n_estados, n_estados), dtype=np.float64)
        for a in range(n_acciones):
            for s in range(n_estados):
                for prob, delta in zip(probs[a], acciones[a]):
                    s_next = np.clip(s + delta, 0, n_estados - 1) # Estado destino con absorción en los extremos
                    P[a][s][s_next] += prob # Acumular la probabilidad para el estado siguiente s_next
        return P



    @staticmethod
    def generate_R() -> np.ndarray:
        """ Function that generates the rewards (costs) matrix """
        ### TO BE COMPLETED BY THE STUDENTS ###
        ...

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
