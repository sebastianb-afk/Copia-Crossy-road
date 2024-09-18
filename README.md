# Proyecto de Pygame: Crossy Road

Este proyecto es una implementación en Pygame de un juego tipo "Crossy Road". El objetivo del juego es guiar a un jugador a través de un entorno lleno de obstáculos y vehículos mientras se intenta alcanzar un objetivo. 

## Descripción General

El juego presenta un menú principal desde el cual el usuario puede acceder a la configuración del juego o comenzar a jugar. En el modo de juego, el jugador controla un rectángulo que debe evitar los obstáculos y vehículos en movimiento para alcanzar una meta.

## Estructura del Código

El código está estructurado en varias clases y funciones clave:

### Clases

#### `Car`
- **Descripción**: Representa un vehículo que se mueve horizontalmente en la pantalla.
- **Atributos**:
  - `rect`: Un objeto `pygame.Rect` que define la posición y tamaño del coche.
  - `speed`: La velocidad a la que se mueve el coche.
  - `direction`: La dirección en la que se mueve el coche (-1 para izquierda, 1 para derecha).
  - `color`: El color del coche, elegido aleatoriamente entre varios tonos de azul.
- **Métodos**:
  - `move(a, u)`: Mueve el coche horizontalmente y rebota en los bordes de la pantalla.
  - `draw(surface)`: Dibuja el coche en la superficie dada.

#### `Solid_object`
- **Descripción**: Representa un objeto sólido en el juego que no se mueve.
- **Atributos**:
  - `rect`: Un objeto `pygame.Rect` que define la posición y tamaño del objeto sólido.
  - `color`: El color del objeto sólido, elegido aleatoriamente entre varios tonos de gris.
- **Métodos**:
  - `draw(surface)`: Dibuja el objeto sólido en la superficie dada.

### Funciones

#### `cars_generator(w, h, u, s)`
- **Descripción**: Genera una lista de objetos `Car` en posiciones aleatorias.
- **Parámetros**:
  - `w`: Ancho de la pantalla en unidades.
  - `h`: Alto de la pantalla en unidades.
  - `u`: Tamaño de la unidad en píxeles.
  - `s`: Velocidad de los coches.
- **Retorna**: Una lista de objetos `Car`.

#### `objects_generator(w, h, u)`
- **Descripción**: Genera una lista de objetos `Solid_object` en posiciones aleatorias con un hueco de 3 posiciones.
- **Parámetros**:
  - `w`: Ancho de la pantalla en unidades.
  - `h`: Alto de la pantalla en unidades.
  - `u`: Tamaño de la unidad en píxeles.
- **Retorna**: Una lista de objetos `Solid_object`.

#### `no_move()`
- **Descripción**: Verifica si no se está presionando ninguna tecla de movimiento.
- **Retorna**: `True` si no se presiona ninguna tecla de movimiento, `False` en caso contrario.

### Flujo del Programa

1. **Inicialización**:
   - Se inicializa Pygame y se configura la pantalla, el reloj y las fuentes.

2. **Menú Principal**:
   - Muestra el menú principal donde el usuario puede elegir entre opciones y jugar.
   - Permite acceder a las configuraciones del juego y comenzar a jugar.

3. **Configuración**:
   - Permite al usuario ajustar el tamaño del bloque y la velocidad del juego.
   - El usuario puede cambiar estas configuraciones presionando las teclas `C` (cambiar tamaño) y `V` (cambiar velocidad).

4. **Modo de Juego**:
   - El jugador controla un rectángulo que debe evitar obstáculos y vehículos.
   - Los vehículos y objetos sólidos se generan dinámicamente.
   - El jugador debe alcanzar el objetivo para ganar el juego.

5. **Pantalla de Victoria**:
   - Se muestra al ganar el juego, con opciones para reiniciar, salir o volver al menú.

## Controles del Juego

- `W`, `A`, `S`, `D`: Mueven al jugador en la pantalla.
- `Q`: Sale del juego.
- `M`: Vuelve al menú principal.
- `R`: Reinicia el juego.
- `C`: Cambia el tamaño del bloque.
- `V`: Cambia la velocidad del juego.
- `O`: Accede a la configuración.

## Requisitos

- Python 3.x
- Pygame (se puede instalar con `pip install pygame`)
