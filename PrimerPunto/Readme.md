# Primer Punto (Transformada de Fourier)

Algunas implementaciones de la transformada de fourier para la capa fisica, la vemos reflejadas principalemente en las señales electromagneticas, como lo es el bluetooth.

Bluetooth es un medio de comunicación inalambrica de corto alcance que opera en la frecuencia de 2.4 GHz, la misma utilizada por Wi-Fi, hornos microondas y otros dispositivos de radiofrecuencia. Debido a que comparte el espectro con varias tecnologias, enfrenta desafios de interferencia, por lo que debe optimizar su transmisión para mantener una conexión estable entre dispositivos.

# Conversión de la señal al dominio de la frecuencia

En su forma original, una señal de Bluetooth se representa en el dominio del tiempo (variacion de amplitud con respecto al tiempo).
Aplicando la Transformada de Fourier, esta señal se convierte en el dominio de la frecuencia, permitiendo visualizar la energía distribuida a lo largo de distintas frecuencias. Es decir que viendo la grafica de la transformada de fourier podemos observar las frecuencias que estan ocupadas por ciertas conexciones al rededor. De esta manera el protocolo bluetooth buscara conexiones con frecuencias en las que no esten ocupadas mediante el uso de AFH.

Adaptive Frequency Hopping (AFH)

Bluetooth emplea una técnica llamada Adaptive Frequency Hopping (AFH), donde salta entre diferentes frecuencias para minimizar la interferencia. La TF ayuda a detectar los canales más congestionados y evitar que Bluetooth los use en su esquema de saltos.

# Modulacion y desmodulacion de la señal
La modulacion consiste en transformar una señal original de baja frecuencia en una señal de alta frecuencia mediante una señal portadora. Esto permite transmitir la información de manera eficiente a través del aire o de cables. Existen varias formas de modulacion, como la AM, FM, SPK, ASK.
La implementacion de fourier en la modulacion y de la desmodulacion de la señal viene cuando la señal va a hacer desmodulada, la TF permite identificar las frecuencias utiles, pudiendole identificar las señales basura/ruido para solo usar las señales que contienen informacion importante.


# Grafica de Fourier
Para esto creamos 3 funciones sinusoidal con diferentes frecuencias e amplitudes:
![alt text](https://github.com/samuelleyton2006/PrimerParcialR--RC/blob/main/PrimerPunto/scr/FUNCIONES.png?raw=true)
Onda 1 con frecuencia 1/10 Hz
Onda 2 con frecuencia 2 Hz
Onda 3 con frecuencia 5 Hz

Ahora, si queremos visualizar la suma de las ondas, podemos hacerlo mediante el uso del programa R, que se encuentra en la carpeta scr.
![alt text](https://github.com/samuelleyton2006/PrimerParcialR--RC/blob/main/PrimerPunto/scr/Sumas.png?raw=true)
Tener encuenta que estas funciones siguen en el dominio del tiempo.
# Transformada de fourier
![alt text](https://github.com/samuelleyton2006/PrimerParcialR--RC/blob/main/PrimerPunto/scr/Transformada.png?raw=true)

