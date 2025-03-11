# Tercer Punto 

``` py
import random

def evento_transmision(probabilidad_exito=0.8):
    """Simula el resultado de una transmisión, devolviendo True si es exitosa."""
    return random.random() < probabilidad_exito

def simular_tcp_congestion(transmisiones=20):
    """Ejecuta una simulación de control de congestión TCP (modelo Tahoe)."""
    ventana_congestion = 1  # Estado inicial de la ventana
    registros = []

    for intento in range(1, transmisiones + 1):
        if evento_transmision():
            ventana_congestion += 1  # Aumenta si la transmisión tiene éxito
            estado = "Éxito"
        else:
            ventana_congestion = 1  # Reinicio en caso de pérdida
            estado = "Pérdida"
        
        registros.append(f"Transmisión {intento}: {estado} - cwnd = {ventana_congestion}")
    
    return registros

def mostrar_evolucion(historial):
    """Imprime el historial de la evolución de la ventana de congestión."""
    for registro in historial:
        print(registro)

# Ejecutar simulación
resultado_tcp = simular_tcp_congestion()
mostrar_evolucion(resultado_tcp)

```
