# Sistema de Control de Reactor Nuclear mediante MDP (Procesos de Decisión de Markov)

**Práctica de Inteligencia Artificial (2025/2026)**
**Autores (NIAs):** 100550288, 100550293, 100550287

## Descripción del Proyecto
Este repositorio contiene la implementación completa de un sistema de control inteligente para un reactor nuclear. El sistema utiliza un modelo de Procesos de Decisión de Markov (MDP) con el algoritmo *Value Iteration* para determinar la política óptima que permite ajustar la potencia del reactor a una curva de demanda energética estocástica, minimizando los errores y penalizaciones.

## Requisitos y Dependencias
Para ejecutar este proyecto, es necesario disponer de Python 3.x y las siguientes librerías instaladas:
- `numpy`
- `matplotlib`
- `pymdptoolbox`

Puedes instalarlas ejecutando:
\`\`\`bash
pip install numpy matplotlib pymdptoolbox
\`\`\`

## Instrucciones de Ejecución
El punto de entrada del programa es el script `main.py`. Se debe ejecutar desde la terminal pasando como argumento el archivo de configuración JSON del reactor que se desea simular.

**Ejecución básica (Reactor RBMK por defecto):**
\`\`\`bash
python main.py --input-reactor Reactors/R0.json
\`\`\`

**Ejecución con parámetros fijos (Recomendado para reproducibilidad):**
Para reproducir exactamente los experimentos detallados en la memoria del proyecto, se recomienda fijar el factor de descuento (`--gamma`) y la semilla aleatoria (`--random-seed`):
\`\`\`bash
python main.py --input-reactor Reactors/R_caotico.json --gamma 0.9 --random-seed 42
\`\`\`

## Estructura de Experimentación (Apartado 4.5)
Además de los reactores base proporcionados (`R0` a `R3`), se han diseñado modelos adicionales en la carpeta `Reactors/` para evaluar la robustez del sistema frente a escenarios extremos:
- `R_ideal.json`: Comportamiento 100% determinista.
- `R_caotico.json` y `R_equi.json`: Entornos de alta incertidumbre/entropía.
- `R_sesgado_bajada.json` y `R_sesgado_subida.json`: Entornos con tendencias opuestas a las acciones de control.
- `R_peligroso.json`: Simulación de un núcleo inestable.

*Nota: Se ha incluido la carpeta `Resultados_Graficos/` con todas las gráficas generadas durante nuestras pruebas de experimentación para su consulta detallada, de modo que la memoria en formato PDF se mantenga concisa y legible.*
