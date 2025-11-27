# Laboratorio No. 04 - 2025-II - Robótica de Desarrollo, Intro a ROS 2 Humble - Turtlesim
El presente informe corresponde al Laboratorio No. 04 , cuyo objetivo principal es introducir al estudiante en el uso de ROS 2 Humble y el simulador Turtlesim como entorno base para el control de robots móviles virtuales. Durante la práctica se exploró el funcionamiento de los nodos, tópicos y mensajes dentro del ecosistema ROS, integrando además los comandos esenciales de Linux para la ejecución y gestión del workspace. Como ejercicio central se desarrolló un script en Python capaz de controlar la tortuga de forma manual mediante el teclado y, adicionalmente, programar el dibujo automático de letras basadas en las iniciales del nombre del usuario. Este laboratorio permitió comprender de manera práctica la estructura modular de ROS, afianzar la comunicación entre nodos y fortalecer habilidades de programación orientadas al control de movimiento, logrando así sentar bases sólidas para el desarrollo de aplicaciones robóticas más avanzadas.
## Metodología
### Diagrama de flujo
flowchart TD

A([Inicio]) --> B[Inicializar rclpy]
B --> C[Crear nodo TurtleController]
C --> D[Esperar servicios:\nTeleportAbsolute / TeleportRelative / SetPen]
D --> E[Configurar tamaño de letras y posiciones]

E --> F{¿Presiona una tecla?}

F -->|Flechas| G[Detectar secuencia de tecla]
G --> H{¿Arriba/Abajo/\nIzquierda/Derecha?}
H -->|Arriba| H1[Llamar move_relative(0.4,0)]
H -->|Abajo| H2[Llamar move_relative(-0.4,0)]
H -->|Derecha| H3[Llamar move_relative(0,-0.9)]
H -->|Izquierda| H4[Llamar move_relative(0,0.9)]
H1 --> F
H2 --> F
H3 --> F
H4 --> F

F -->|Letra L| I[Llamar draw_L()]
F -->|Letra N| J[Llamar draw_N()]
F -->|Letra F| K[Llamar draw_F()]
F -->|Letra D| L[Llamar draw_D()]
F -->|Letra G| M[Llamar draw_G()]
F -->|Letra P| N[Llamar draw_P()]

I --> F
J --> F
K --> F
L --> F
M --> F
N --> F

F -->|Letra Q| O([Salir del programa])
O --> P[Destruir nodo]
P --> Q([Shutdown rclpy])
Q --> R([Fin])

### Código diseñado
[Programa move_turtle](./move_turtle.py)
## Análisis y Resultados
### Video de Demostración
## Conclusiones

