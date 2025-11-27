# Laboratorio No. 04 - 2025-II - Robótica de Desarrollo, Intro a ROS 2 Humble - Turtlesim
El presente informe corresponde al Laboratorio No. 04 , cuyo objetivo principal es introducir al estudiante en el uso de ROS 2 Humble y el simulador Turtlesim como entorno base para el control de robots móviles virtuales. Durante la práctica se exploró el funcionamiento de los nodos, tópicos y mensajes dentro del ecosistema ROS, integrando además los comandos esenciales de Linux para la ejecución y gestión del workspace. Como ejercicio central se desarrolló un script en Python capaz de controlar la tortuga de forma manual mediante el teclado y, adicionalmente, programar el dibujo automático de letras basadas en las iniciales del nombre del usuario. Este laboratorio permitió comprender de manera práctica la estructura modular de ROS, afianzar la comunicación entre nodos y fortalecer habilidades de programación orientadas al control de movimiento, logrando así sentar bases sólidas para el desarrollo de aplicaciones robóticas más avanzadas.
## Metodología
### Diagrama de flujo
```mermaid
flowchart TD

A([Inicio]) --> B[Inicializar rclpy]
B --> C[Crear nodo TurtleController]
C --> D[Esperar servicios\nTeleportAbs / TeleportRel / SetPen]
D --> E[Configurar tamaños y posiciones de letras]

E --> F{¿Tecla presionada?}

%% --- Movimiento con flechas ---
F -->|Flechas| G[Leer comando direccional]
G --> H{¿Qué flecha?}
H -->|Arriba| H1[move_relative(0.4,0)]
H -->|Abajo| H2[move_relative(-0.4,0)]
H -->|Derecha| H3[move_relative(0,-0.9)]
H -->|Izquierda| H4[move_relative(0,0.9)]
H1 --> F
H2 --> F
H3 --> F
H4 --> F

%% --- Letras a dibujar ---
F -->|L| I[draw_L()]
F -->|N| J[draw_N()]
F -->|F| K[draw_F()]
F -->|D| L[draw_D()]
F -->|G| M[draw_G()]
F -->|P| N[draw_P()]

I --> F
J --> F
K --> F
L --> F
M --> F
N --> F

%% --- Salida ---
F -->|Q| O([Salir])
O --> P[Destruir nodo]
P --> Q([rclpy.shutdown()])
Q --> R([Fin])
```

### Código diseñado
[Programa move_turtle](./move_turtle.py)
## Análisis y Resultados
### Video de Demostración
## Conclusiones

