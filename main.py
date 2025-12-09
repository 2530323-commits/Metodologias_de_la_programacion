import network
import socket
from machine import Pin, PWM
import time

# ---------------------------
# CONFIGURACIÓN DE MOTORES
# ---------------------------

# Motor izquierdo
IN1 = Pin(25, Pin.OUT)
IN2 = Pin(33, Pin.OUT)
ENA = PWM(Pin(32))
ENA.freq(1000)

# Motor derecho
IN3 = Pin(14, Pin.OUT)
IN4 = Pin(27, Pin.OUT)
ENB = PWM(Pin(26))
ENB.freq(1000)

# Velocidad inicial (0–1023)
speed = 500

# ---------------------------
# FUNCIONES DE MOVIMIENTO
# ---------------------------

def stop():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    ENA.duty(0)
    ENB.duty(0)

def forward():
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    ENA.duty(speed)
    ENB.duty(speed)

def backward():
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)
    ENA.duty(speed)
    ENB.duty(speed)

def left():
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)
    ENA.duty(speed)
    ENB.duty(speed)

def right():
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    ENA.duty(speed)
    ENB.duty(speed)

# ---------------------------
# FUNCIÓN PARA CAMBIAR LA VELOCIDAD
# ---------------------------

def set_speed(value):
    global speed
    speed = value
    print("Nueva velocidad:", speed)

stop()

# ---------------------------
# CONEXIÓN WIFI MODO AP
# ---------------------------

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="CarritoESP32", password="12345678")

print("Conéctate al WiFi: CarritoESP32")
print("Contraseña: 12345678")
print("IP:", ap.ifconfig()[0])

# ---------------------------
# SERVIDOR WEB
# ---------------------------

def pagina_web():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Carrito ESP32</title>
      <style>
        body { text-align: center; font-family: Arial; }
        button {
            width: 120px; height: 60px;
            font-size: 20px; margin: 10px;
        }
      </style>
    </head>
    <body>
      <h1>Control del Carrito ESP32</h1>

      <button onclick="location.href='/forward'">⬆ Adelante</button><br>
      <button onclick="location.href='/left'">⬅ Izquierda</button>
      <button onclick="location.href='/stop'">⛔ Stop</button>
      <button onclick="location.href='/right'">Derecha ➡</button><br>
      <button onclick="location.href='/backward'">⬇ Atrás</button>

      <h2>Velocidad</h2>
      <button onclick="location.href='/speed_low'">Lenta</button>
      <button onclick="location.href='/speed_mid'">Media</button>
      <button onclick="location.href='/speed_fast'">Rápida</button>
      <button onclick="location.href='/speed_max'">Máxima</button>

    </body>
    </html>
    """
    return html


# Crear servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 80))
s.listen(5)

print("Servidor web listo!")

while True:
    conn, addr = s.accept()
    print("Conexión desde:", addr)
    request = conn.recv(1024).decode()

    # ---------------------------
    # RUTAS DE MOVIMIENTO
    # ---------------------------

    if "/forward" in request:
        forward()
    elif "/backward" in request:
        backward()
    elif "/left" in request:
        left()
    elif "/right" in request:
        right()
    elif "/stop" in request:
        stop()

    # ---------------------------
    # RUTAS DE VELOCIDAD
    # ---------------------------

    elif "/speed_low" in request:
        set_speed(350)
    elif "/speed_mid" in request:
        set_speed(600)
    elif "/speed_fast" in request:
        set_speed(850)
    elif "/speed_max" in request:
        set_speed(1023)

    response = pagina_web()
    conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    conn.sendall(response)
    conn.close()
