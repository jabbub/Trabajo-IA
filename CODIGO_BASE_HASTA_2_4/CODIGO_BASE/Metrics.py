# Import required dependencies
import numpy as np

def MAE(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the Mean Absolute Error (MAE) """
    ### TO BE COMPLETED BY THE STUDENTS ###

    # Calculamos el promedio de los errores absolutos
    errors = np.abs(y_true - y_pred)
    mae = np.mean(errors)

    return np.float64(mae)
    ### ###

def MSE(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the Mean Squared Error (MSE) """
    ### TO BE COMPLETED BY THE STUDENTS ###

    # Calculamos el promedio de los errores al cuadrado
    errors = (y_true - y_pred) ** 2
    mse = np.mean(errors)

    return np.float64(mse)
    ### ###

def R2(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the R2 metric """
    ### TO BE COMPLETED BY THE STUDENTS ###

    # Suma de cuadrados de los errores
    ss_res = np.sum((y_true - y_pred) ** 2)

    # Suma de cuadrados respecto a la media real
    y_mean = np.mean(y_true)
    ss_tot = np.sum((y_true - y_mean) ** 2)

    # Si todos los valores reales son iguales, evitamos dividir entre cero
    if ss_tot == 0:
        return np.float64(0.0)

    r2 = 1 - (ss_res / ss_tot)

    return np.float64(r2)
    ### ###

def Corr(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the Pearson's Correlation Coefficient """
    ### TO BE COMPLETED BY THE STUDENTS ###

    # Si alguna señal no varía, la correlación no se puede calcular correctamente
    if np.std(y_true) == 0 or np.std(y_pred) == 0:
        return np.float64(0.0)

    # np.corrcoef devuelve una matriz 2x2; el valor [0,1] es la correlación
    corr_matrix = np.corrcoef(y_true, y_pred)
    corr = corr_matrix[0, 1]

    return np.float64(corr)
    ### ###
    