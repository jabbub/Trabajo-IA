# Import required dependencies
import numpy as np
import mdptoolbox

class ControlModule:
    def __init__(self):
        """ Dummy constructor to use the Python Class as a namespace """
        pass

    @staticmethod
    def generate_P(probs: np.ndarray,
                   n_states: np.int32,
                   n_actions: np.int32) -> np.ndarray:
        """ Function that generates the probabilities (transition) matrix """

        # Creamos la matriz de transicion: acciones x estados origen x estados destino
        P = np.zeros((n_actions, n_states, n_states), dtype=np.float64)

        # Desplazamientos posibles de cada accion
        movements = [
            [-2, -1, 0], # Accion 0: decrementar
            [-1,  0, 1], # Accion 1: mantener
            [ 0,  1, 2]  # Accion 2: incrementar
        ]

        # Recorremos todas las acciones y todos los estados
        for action in range(n_actions):
            for state in range(n_states):
                for i, delta in enumerate(movements[action]):

                    # np.clip evita que el estado destino salga del rango permitido
                    next_state = np.clip(state + delta, 0, n_states - 1)

                    # Sumamos la probabilidad correspondiente.
                    # En los extremos, varias transiciones pueden acabar en el mismo estado.
                    P[action, state, next_state] += probs[action][i]

        return P

    @staticmethod
    def generate_C(demand_t: np.float64,
                   n_states: np.int32,
                   n_actions: np.int32) -> np.ndarray:
        """ Function that generates the costs matrix """

        # Creamos la matriz de costes: acciones x estados origen x estados destino
        C = np.zeros((n_actions, n_states, n_states), dtype=np.float64)

        for next_state in range(n_states):

            # Potencia asociada al estado destino.
            # Por ejemplo, el estado 50 representa aproximadamente 0.50
            next_power = next_state / n_states

            # Coste base: distancia entre la demanda y la potencia final
            base_cost = abs(demand_t - next_power)

            for action in range(n_actions):
                cost = base_cost

                # Penalizamos acciones contradictorias:
                # - incrementar cuando la potencia final queda por encima de la demanda
                # - decrementar cuando la potencia final queda por debajo de la demanda
                if action == 2 and next_power > demand_t:
                    cost *= 2.0
                elif action == 0 and next_power < demand_t:
                    cost *= 2.0

                # El coste depende del estado destino y de la accion, no del estado origen
                C[action, :, next_state] = cost

        return C

    @staticmethod
    def generate_R(demand_t: np.float64,
                   n_states: np.int32,
                   n_actions: np.int32) -> np.ndarray:
        """ Function that generates the rewards (costs) matrix """

        # La libreria mdptoolbox trabaja con recompensas.
        # Como nuestro modelo usa costes, usamos R = -C.
        C = ControlModule.generate_C(demand_t, n_states, n_actions)
        R = -C

        return R

    @staticmethod
    def control_iteration(current_state: np.int32,
                          demand_t: np.float64,
                          P: np.ndarray,
                          n_states: np.int32,
                          n_actions: np.int32,
                          gamma: np.float64) -> np.int32:
        """ Function that computes one control-iteration """

        # Generamos la matriz de recompensas para la demanda actual
        R = ControlModule.generate_R(demand_t, n_states, n_actions)

        # Resolvemos el MDP mediante Iteracion de Valores
        vi = mdptoolbox.mdp.ValueIteration(P, R, gamma)
        vi.run()

        # La politica contiene la mejor accion para cada estado
        policy = vi.policy

        # Devolvemos solo la accion correspondiente al estado actual
        action = policy[current_state]

        return np.int32(action)

    @staticmethod
    def control_loop(demand: np.ndarray, 
                     probs: np.ndarray,
                     n_states: np.int32, 
                     n_actions: np.int32,
                     gamma: np.float64) -> np.ndarray:
        """ Function that computes all the required iterations (control-loop) to satisfy the power demand """
        ### TO BE COMPLETED BY THE STUDENTS ###

        # Creamos el vector donde se guarda la respuesta del reactor
        response = np.zeros_like(a=demand, dtype=np.float64)

        # La matriz P solo depende del reactor, por eso se calcula una sola vez
        P = ControlModule.generate_P(probs, n_states, n_actions)

        # Suponemos que el reactor empieza en el nivel minimo de potencia
        current_state = 0

        # Recorremos todos los instantes de la demanda
        for t in range(demand.shape[0]):

            # Demanda del instante actual
            demand_t = demand[t]

            # Obtenemos la mejor accion para el estado actual
            action = ControlModule.control_iteration(current_state,
                                                     demand_t,
                                                     P,
                                                     n_states,
                                                     n_actions,
                                                     gamma)

            # Probabilidades de transicion para la accion elegida
            probabilities = P[action, current_state, :]

            # Normalizamos para evitar pequenos errores numericos
            probabilities = probabilities / np.sum(probabilities)

            # Simulamos el siguiente estado del reactor
            current_state = np.random.choice(a=n_states, p=probabilities)

            # Guardamos la potencia producida en escala [0, 1]
            response[t] = current_state / n_states

        return response
        ### ###
        