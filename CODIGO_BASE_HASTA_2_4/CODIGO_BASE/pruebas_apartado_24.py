import numpy as np
from Metrics import MAE, MSE, R2, Corr


# Datos sencillos de prueba
y_true = np.array([0.10, 0.20, 0.30, 0.40, 0.50], dtype=np.float64)
y_pred = np.array([0.12, 0.18, 0.33, 0.37, 0.52], dtype=np.float64)

mae = MAE(y_true, y_pred)
mse = MSE(y_true, y_pred)
r2 = R2(y_true, y_pred)
corr = Corr(y_true, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R2:", r2)
print("Correlacion de Pearson:", corr)

# Comprobaciones basicas
if mae >= 0:
    print("MAE correcto: no puede ser negativo")

if mse >= 0:
    print("MSE correcto: no puede ser negativo")

if corr >= -1 and corr <= 1:
    print("Correlacion correcta: esta dentro de [-1, 1]")
    