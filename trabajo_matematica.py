import pygame
import math

# Configuración inicial
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Definición del vehículo
class Vehiculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # Ángulo de dirección en grados
        self.speed = 0  # Velocidad inicial

    def mover(self):
        # Movimiento basado en la velocidad y el ángulo
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def girar(self, angulo):
        # Rotación del vehículo
        self.angle += angulo

    def acelerar(self, incremento):
        # Aumentar o reducir la velocidad
        self.speed += incremento

    def detectar_colision(self, obstaculo_rect):
        # Detección de colisión con un obstáculo
        vehiculo_rect = pygame.Rect(self.x, self.y, 40, 20)
        return vehiculo_rect.colliderect(obstaculo_rect)

# Definición de un potenciador
class Potenciador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 20, 20)

    def recoger(self, vehiculo):
        # Detección de proximidad entre el vehículo y el potenciador
        distancia = math.hypot(self.x - vehiculo.x, self.y - vehiculo.y)
        if distancia < 30:
            return True
        return False

# Inicialización del vehículo y el potenciador
vehiculo = Vehiculo(400, 300)
potenciador = Potenciador(600, 300)
obstaculo = pygame.Rect(300, 300, 50, 50)

# Loop principal del juego
running = True
while running:
    screen.fill((0, 0, 0))

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control del vehículo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vehiculo.girar(-5)
    if keys[pygame.K_RIGHT]:
        vehiculo.girar(5)
    if keys[pygame.K_UP]:
        vehiculo.acelerar(0.2)
    if keys[pygame.K_DOWN]:
        vehiculo.acelerar(-0.2)

    # Mover el vehículo y detectar colisiones
    vehiculo.mover()
    if vehiculo.detectar_colision(obstaculo):
        print("¡Colisión con obstáculo!")

    # Detección de potenciador
    if potenciador.recoger(vehiculo):
        print("¡Potenciador recogido!")

    # Dibujar el vehículo, el potenciador y el obstáculo
    pygame.draw.rect(screen, (255, 0, 0), (vehiculo.x, vehiculo.y, 40, 20))  # Vehículo
    pygame.draw.rect(screen, (0, 255, 0), potenciador.rect)  # Potenciador
    pygame.draw.rect(screen, (0, 0, 255), obstaculo)  # Obstáculo

    pygame.display.flip()
    clock.tick(30)

pygame.quit()