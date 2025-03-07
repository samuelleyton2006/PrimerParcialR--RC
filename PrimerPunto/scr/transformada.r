library(plotly)
time <- 200
fs <- 100  # Frecuencia de muestreo
dt <- 1/fs
t <- seq(0, time, by=dt)  # Vector de tiempo

# Generar ondas
wave.1 <- 2*sin(2*pi*(1/10)*t)  # Onda 1 con frecuencia 1/10 Hz
wave.2 <- 1*sin(2*pi*2*t)      # Onda 2 con frecuencia 2 Hz
wave.3 <- 0.5*sin(2*pi*(5)*t) # Onda 3 con frecuencia 5 Hz

# Crear DataFrame para la gráfica de señales
data <- data.frame(t, wave.1, wave.2, wave.3)

# Graficar las ondas
fig1 <- plot_ly(data, x=~t, y=~wave.1, name="Onda 1", type="scatter", mode="lines") %>%
    add_trace(y=~wave.2, name='Onda 2', mode="lines") %>%
    add_trace(y=~wave.3, name="Onda 3", mode="lines") %>%
    layout(title="Ondas en el tiempo", xaxis=list(range=c(0,20), title="Tiempo (s)"), yaxis=list(title="Amplitud"))

# Mostrar la gráfica correctamente en VS Code
if (interactive()) fig1 else htmlwidgets::saveWidget(fig1, "ondas.html", selfcontained = TRUE)

# Suma de ondas
x <- wave.1 + wave.2 + wave.3

# DataFrame para la onda combinada
data_sum <- data.frame(t, x)

# Graficar la señal combinada
fig2 <- plot_ly(data_sum, x=~t, y=~x, type="scatter", mode="lines") %>%
    layout(title="Suma de ondas", xaxis=list(range=c(0,20), title="Tiempo (s)"), yaxis=list(title="Amplitud"))

if (interactive()) fig2 else htmlwidgets::saveWidget(fig2, "suma_ondas.html", selfcontained = TRUE)

# **ESPECTRO DE FRECUENCIAS**
x.spec <- spectrum(x, plot=FALSE)  # Evitar que genere una gráfica por defecto
spx <- x.spec$freq * fs            # Convertir frecuencias normalizadas a Hz
spy <- 2 * x.spec$spec              # Ajustar la densidad espectral

# DataFrame para la gráfica espectral
data_spec <- data.frame(f=spx, espectro=spy)

# Graficar el espectro de frecuencia
fig3 <- plot_ly(data_spec, x=~f, y=~espectro, type="scatter", mode="lines") %>%
    layout(title="Espectro de frecuencia", 
           xaxis=list(range=c(0,5), title="Frecuencia (Hz)"), 
           yaxis=list(title="Densidad de frecuencia"))

if (interactive()) fig3 else htmlwidgets::saveWidget(fig3, "espectro.html", selfcontained = TRUE)
