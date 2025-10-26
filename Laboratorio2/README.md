# Laboratorio No. 02 Robótica Industrial - Análisis y Operación del Manipulador Motoman MH6.
## Cuadro Comparativo Motoman MH6 y el IRB140
Una línea en blanco antes de la tabla es importante para que se muestre correctamente.

| Característica                       | Motoman MH6      | ABB IRB 140                                   |
|------------------------------------|------------------------------------------------|----------------------------------------------|
| Grados de libertad          | 8                           | 6                            |
| Carga máxima (payload)             | Aproximadamente 6 kg  | Aproximadamente 6 kg                           |
| Alcance (reach / H-reach)          | ≈ 1.422 m                                     | ≈ 0.810 m                                     |
| Repetibilidad (posición)           | ±0.08 mm                                       | ≈ ±0.02-0.06 mm      |
| Velocidades (ejemplos / máximas)   | Ej.: S~140°/s, L~130°/s, U~135°/s, R~270°/s, B~270°/s, T~400°/s (MH6-10) | Velocidades altas para su tamaño; cifras específicas dependen de configuración |
| Masa / peso del manipulador        | ≈ 130 kg                                       | Variable según versión; ≈ 98-100 kg para algunas variantes |
| Montaje                            | Piso, invertido, montaje angular/ángulo        | Piso, invertido o pared/suspensión en cualquier ángulo |
| Protección / versiones especiales  | Variantes estándar para ambientes industriales | Versiones Standard, Foundry, Clean Room, Wash (IP67) |
| Controlador                        | Usualmente DX100 (o DXM/FS100 en variantes)    | Controladores ABB S4Cplus u otros según versión |
| Aplicaciones típicas               | Machine tending, manejo de materiales, montaje, soldadura, pick & place | Manejo de materiales, machine tending, empaquetado, soldadura, limpieza/spray |
| Ventajas destacadas                | Gran alcance relativo, variantes de mayor carga | Compacto, alta agilidad, montaje flexible    |
| Consideraciones / limitaciones     | Verificar versión (6 kg vs 10 kg), integración del controlador | Alcance menor que MH6; verificar versión concreta |


## Descripción de Configuración de los homes del Motoman MH6
### Home 1
### Home 2
## Procedimiento de movimientos Manuales 
## Niveles de velocidad para movimientos manuales
## Principales funcionalidades de RoboDK
## Comparación RoboDK y RobotStudio
## Diagrama de flujo de acciones del robot Motoman MH6
<p align="center">
<img src="./Diagrama_Flujo.png" width="200">
</p>

## Plano de planta
## Código desarrollado en RoboDK
## Video de simulación en RoboDK e implementación en robot Motoman MH6
