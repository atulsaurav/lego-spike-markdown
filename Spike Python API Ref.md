
# API Modules

## App
The `app` module is used communicate between hub and app
### Sub Modules

### Bargraph
The `bargraph` module is used make bar graphs in the SPIKE AppTo use the `bargraph` module simply import the module like so:
```python
from app import bargraph
```
`bargraph` details
#### Functions

#### `change`
`change(color: int, value: float) -> None`

##### Parameters
----------
##### `color: int`
A color from the `color` module
##### `value: float`
 The value
#### `clear_all`
`clear_all() -> None`

##### Parameters
----------
#### `get_value`
`get_value(color: int) -> Awaitable`

##### Parameters
----------
##### `color: int`
A color from the `color` module
#### `hide`
`hide() -> None`

##### Parameters
----------
#### `set_value`
`set_value(color: int, value: float) -> None`

##### Parameters
----------
##### `color: int`
A color from the `color` module
##### `value: float`
 The value
#### `show`
`show(fullscreen: bool) -> None`

##### Parameters
----------
##### `fullscreen: bool`
Show in full screen
### Display
The `display` module is used show images in the SPIKE AppTo use the `display` module simply import the module like so:
```python
from app import display
```
`display` details
#### Functions

#### `hide`
`hide() -> None`

##### Parameters
----------
#### `image`
`image(image: int) -> None`

##### Parameters
----------
##### image: int
The id of the image to show. The range of available images is 1 to 21. There are consts on the `display` module for these
#### `show`
`show(fullscreen: bool) -> None`

##### Parameters
----------
##### `fullscreen: bool`
Show in full screen
#### `text`
`text(text: str) -> None`

##### Parameters
----------
##### `text: str`
The text to display
#### Constants
----------
#### `app.display` Constants
`IMAGE_ROBOT_1` = 1

`IMAGE_ROBOT_2` = 2

`IMAGE_ROBOT_3` = 3

`IMAGE_ROBOT_4` = 4

`IMAGE_ROBOT_5` = 5

`IMAGE_HUB_1` = 6

`IMAGE_HUB_2` = 7

`IMAGE_HUB_3` = 8

`IMAGE_HUB_4` = 9

`IMAGE_AMUSEMENT_PARK` = 10

`IMAGE_BEACH` = 11

`IMAGE_HAUNTED_HOUSE` = 12

`IMAGE_CARNIVAL` = 13

`IMAGE_BOOKSHELF` = 14

`IMAGE_PLAYGROUND` = 15

`IMAGE_MOON` = 16

`IMAGE_CAVE` = 17

`IMAGE_OCEAN` = 18

`IMAGE_POLAR_BEAR` = 19

`IMAGE_PARK` = 20

`IMAGE_RANDOM` = 21

### Linegraph
The `linegraph` module is used make line graphs in the SPIKE AppTo use the `linegraph` module simply import the module like so:
```python
from app import linegraph
```
`linegraph` details
#### Functions

#### `clear`
`clear(color: int) -> None`

##### Parameters
----------
##### `color: int`
A color from the `color` module
#### `clear_all`
`clear_all() -> None`

##### Parameters
----------
#### `get_average`
`get_average(color: int) -> Awaitable`

##### Parameters
----------
##### `color: int`
A color from the `color` module
#### `get_last`
`get_last(color: int) -> Awaitable`

##### Parameters
----------
##### `color: int`
A color from the `color` module
#### `get_max`
`get_max(color: int) -> Awaitable`

##### Parameters
----------
##### `color: int`
A color from the `color` module
#### `get_min`
`get_min(color: int) -> Awaitable`

##### Parameters
----------
##### `color: int`
A color from the `color` module
#### `hide`
`hide() -> None`

##### Parameters
----------
#### `plot`
`plot(color: int, x: float, y: float) -> None`

##### Parameters
----------
##### `color: int`
A color from the `color` module
##### `x: float`
The X value
##### `y: float`
The Y value
#### `show`
`show(fullscreen: bool) -> None`

##### Parameters
----------
##### `fullscreen: bool`
Show in full screen
### Music
The `music` module is used make music in the SPIKE AppTo use the `music` module simply import the module like so:
```python
from app import music
```
`music` details
#### Functions

#### `play_drum`
`play_drum(drum: int) -> None`

##### Parameters
----------
##### `drum: int`
The drum name. See all available values in the app.sound module.
#### `play_instrument`
`play_instrument(instrument: int, note: int, duration: int) -> None`

##### Parameters
----------
##### `instrument: int`
The instrument name. See all available values in the app.music module.
##### `note: int`
The midi note to play (0-130)
##### `duration: int`
The duration in milliseconds
#### Constants
----------
#### `app.music` Constants
`DRUM_BASS` = 2

`DRUM_BONGO` = 13

`DRUM_CABASA` = 15

`DRUM_CLAVES` = 9

`DRUM_CLOSED_HI_HAT` = 6

`DRUM_CONGA` = 14

`DRUM_COWBELL` = 11

`DRUM_CRASH_CYMBAL` = 4

`DRUM_CUICA` = 18

`DRUM_GUIRO` = 16

`DRUM_HAND_CLAP` = 8

`DRUM_OPEN_HI_HAT` = 5

`DRUM_SIDE_STICK` = 3

`DRUM_SNARE` = 1

`DRUM_TAMBOURINE` = 7

`DRUM_TRIANGLE` = 12

`DRUM_VIBRASLAP` = 17

`DRUM_WOOD_BLOCK` = 10

`INSTRUMENT_BASS` = 6

`INSTRUMENT_BASSOON` = 14

`INSTRUMENT_CELLO` = 8

`INSTRUMENT_CHOIR` = 15

`INSTRUMENT_CLARINET` = 10

`INSTRUMENT_ELECTRIC_GUITAR` = 5

`INSTRUMENT_ELECTRIC_PIANO` = 2

`INSTRUMENT_FLUTE` = 12

`INSTRUMENT_GUITAR` = 4

`INSTRUMENT_MARIMBA` = 19

`INSTRUMENT_MUSIC_BOX` = 17

`INSTRUMENT_ORGAN` = 3

`INSTRUMENT_PIANO` = 1

`INSTRUMENT_PIZZICATO` = 7

`INSTRUMENT_SAXOPHONE` = 11

`INSTRUMENT_STEEL_DRUM` = 18

`INSTRUMENT_SYNTH_LEAD` = 20

`INSTRUMENT_SYNTH_PAD` = 21

`INSTRUMENT_TROMBONE` = 9

`INSTRUMENT_VIBRAPHONE` = 16

`INSTRUMENT_WOODEN_FLUTE` = 13

### Sound
The `sound` module is used play sounds in the SPIKE AppTo use the `sound` module simply import the module like so:
```python
from app import sound
```
`sound` details
#### Functions

#### `play`
`play(sound_name: str, volume: int = 100, pitch: int = 0, pan: int = 0) -> Awaitable`
Play a sound in the SPIKE App
##### Parameters
----------
##### `sound_name: str`
The sound name as seen in the Word Blocks sound extension
##### `volume: int`
The volume (0-100)
##### `pitch: int`
The pitch of the sound
##### `pan: int`
The pan effect determines which speaker is emitting the sound, with "-100" being only the left speaker, "0" being normal, and "100" being only the right speaker.
#### `set_attributes`
`set_attributes(volume: int, pitch: int, pan: int) -> None`

##### Parameters
----------
##### `volume: int`
The volume (0-100)
##### `pitch: int`
The pitch of the sound
##### `pan: int`
The pan effect determines which speaker is emitting the sound, with "-100" being only the left speaker, "0" being normal, and "100" being only the right speaker.
#### `stop`
`stop() -> None`

##### Parameters
----------
## Color
The `color` module contains all the color constants to use with the `color_matrix`, `color_sensor` and `light` modules.To use the Color module add the following import statement to your project:
```python
import color
```

### Constants
----------
### `color` Constants
`BLACK` = 0

`MAGENTA` = 1

`PURPLE` = 2

`BLUE` = 3

`AZURE` = 4

`TURQUOISE` = 5

`GREEN` = 6

`YELLOW` = 7

`ORANGE` = 8

`RED` = 9

`WHITE` = 10

`UNKNOWN` = -1

## Color Matrix
To use the Color Matrix module add the following import statement to your project:
```python
import color_matrix
```
All functions in the module should be called inside the `color_matrix` module as a prefix like so:
```python
color_matrix.set_pixel(port.A, 1, 1, (color.BLUE, 10))
```

### Functions

### `clear`
`clear(port: int) -> None`
Turn off all pixels on a Color Matrix
```python
from hub import port
import color_matrix

color_matrix.clear(port.A)
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `get_pixel`
`get_pixel(port: int, x: int, y: int) -> tuple[int, int]`
Retrieve a specific pixel represented as a tuple containing the color and intensity
```python
from hub import port
import color_matrix

# Print the color and intensity of the 0,0 pixel on the Color Matrix connected to port A 
print(color_matrix.get_pixel(port.A, 0, 0))
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `x: int`
The X value (0 - 2)
#### `y: int`
The Y value, range (0 - 2)
### `set_pixel`
`set_pixel(port: int, x: int, y: int, pixel: tuple[color: int, intensity: int]) -> None`
Change a single pixel on a Color Matrix
```python
from hub import port
import color
import color_matrix

# Change the color of the 0,0 pixel on the Color Matrix connected to port A 
color_matrix.set_pixel(port.A, 0, 0, (color.RED, 10))

# Print the color of the 0,0 pixel on the Color Matrix connected to port A 
print(color_matrix.get_pixel(port.A, 0, 0)[0])
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `x: int`
The X value (0 - 2)
#### `y: int`
The Y value, range (0 - 2)
#### pixel: tuple[color: int, intensity: int]
Tuple containing color and intensity, meaning how bright to light up the pixel
### `show`
`show(port: int, pixels: list[tuple[int, int]]) -> None`
Change all pixels at once on a Color Matrix
```python
from hub import port
import color
import color_matrix

# Update all pixels on Color Matrix using the show function 

# Create a list with 18 items (color and intensity pairs) 
pixels = [(color.BLUE, 10)] * 9 

# Update all pixels to show same color and intensity 
color_matrix.show(port.A, pixels)
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `pixels: list[tuple[int, int]]`
A list containing color and intensity value tuples for all 9 pixels.
## Color Sensor
The `color_sensor` module enables you to write code that reacts to specific colors or the intensity of the reflected light.To use the Color Sensor module add the following import statement to your project:
```python
import color_sensor
```
All functions in the module should be called inside the `color_sensor` module as a prefix like so:
```python
color_sensor.reflection(port.A)
```
The Color Sensor can recognize the following colors:

Red
Green
Blue
Magenta
Yellow
Orange
Azure
Black
White
### Functions

### `color`
`color(port: int) -> int`
Returns the color value of the detected color. Use the `color` module to map the color value to a specific color.
```python
import color_sensor
from hub import port
import color

if color_sensor.color(port.A) is color.RED:
    print("Red detected")
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `reflection`
`reflection(port: int) -> int`
Retrieves the intensity of the reflected light (0-100%).
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `rgbi`
`rgbi(port: int) -> tuple[int, int, int, int]`
Retrieves the overall color intensity and intensity of red, green and blue.Returns `tuple[red: int, green: int, blue: int, intensity: int]`
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
## Device
The `device` module enables you to write code to get information about devices plugged into the hub.To use the Device module add the following import statement to your project:
```python
import device
```
All functions in the module should be called inside the `device` module as a prefix like so:
```python
device.device_id(port.A)
```

### Functions

### `data`
`data(port: int) -> tuple[int]`
Retrieve the raw LPF-2 data from a device.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `id`
`id(port: int) -> int`
Retrieve the device id of a device. Each device has an id based on its type.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `get_duty_cycle`
`get_duty_cycle(port: int) -> int`
Retrieve the duty cycle for a device. Returned values is in range 0 to 10000
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `ready`
`ready(port: int) -> bool`
When a device is attached to the hub it might take a short amount of time before it's ready to accept requests.
Use `ready` to test for the readiness of the attached devices.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `set_duty_cycle`
`set_duty_cycle(port: int, duty_cycle: int) -> None`
Set the duty cycle on a device. Range 0 to 10000
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `duty_cycle: int`
The PWM value (0-10000)
## Distance Sensor
The `distance_sensor` module enables you to write code that reacts to specific distances or light up the  Distance Sensor in different ways.To use the Distance Sensor module add the following import statement to your project:
```python
import distance_sensor
```
All functions in the module should be called inside the `distance_sensor` module as a prefix like so:
```python
distance_sensor.distance(port.A)
```

### Functions

### `clear`
`clear(port: int) -> None`
Turns off all the lights in the Distance Sensor connected to `port`.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `distance`
`distance(port: int) -> int`
Retrieve the distance in millimeters captured by the Distance Sensor connected to `port`. If the Distance Sensor cannot read a valid distance it will return -1.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `get_pixel`
`get_pixel(port: int, x: int, y: int) -> int`
Retrieve the intensity of a specific light on the Distance Sensor connected to `port`.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `x: int`
The X value (0 - 3)
#### `y: int`
The Y value, range (0 - 3)
### `set_pixel`
`set_pixel(port: int, x: int, y: int, intensity: int) -> None`
Changes the intensity of a specific light on the Distance Sensor connected to `port`.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `x: int`
The X value (0 - 3)
#### `y: int`
The Y value, range (0 - 3)
#### `intensity: int`
How bright to light up the pixel
### `show`
`show(port: int, pixels: list[int]) -> None`
Change all the lights at the same time.
```python
from hub import port
import distance_sensor

# Update all pixels on Distance Sensor using the show function 

# Create a list with 4 identical intensity values 
pixels = [100] * 4 

# Update all pixels to show same intensity 
distance_sensor.show(port.A, pixels)
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `pixels: bytes`
A list containing intensity values for all 4 pixels.
## Force Sensor
The `force_sensor` module contains all functions and constants to use the Force Sensor.

To use the Force Sensor module add the following import statement to your project:
```python
import force_sensor
```
All functions in the module should be called inside the `force_sensor` module as a prefix like so:
```python
force_sensor.force(port.A)
```

### Functions

### `force`
`force(port: int) -> int`
Retrieves the measured force as decinewton. Values range from 0 to 100
```python
from hub import port
import force_sensor


print(force_sensor.force(port.A))
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `pressed`
`pressed(port: int) -> bool`
Tests whether the button on the sensor is pressed. Returns true if the force sensor connected to port is pressed.
```python
from hub import port
import force_sensor


print(force_sensor.pressed(port.A))
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `raw`
`raw(port: int) -> int`
Returns the raw, uncalibrated force value of the force sensor connected on port `port`
```python
from hub import port
import force_sensor


print(force_sensor.raw(port.A))
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
## Hub

### Sub Modules

### Button
To use the Button module add the following import statement to your project:
```python
from hub import button
```
All functions in the module should be called inside the `button` module as a prefix like so:
```python
button.pressed(button.LEFT)
```

#### Functions

#### `pressed`
`int pressed(button: int) -> int`
This module allows you to react to buttons being pressed on the hub. You must first import the `button` module to use the buttons.
```python
from hub import button

left_button_press_duration = 0

# Wait for the left button to be pressed 
while not button.pressed(button.LEFT):
    pass

# As long as the left button is being pressed, update the `left_button_press_duration` variable 
while button.pressed(button.LEFT):
    left_button_press_duration = button.pressed(button.LEFT)

print("Left button was pressed for " + str(left_button_press_duration) + " milliseconds")

```

##### Parameters
----------
##### `button: int`
A button from the `button` submodule in the `hub` module
#### Constants
----------
#### `hub.button` Constants
`LEFT` = 1
Left button next to the power button on the SPIKE Prime hub
`RIGHT` = 2
Right button next to the power button on the SPIKE Prime hub
### Light
The `light` module includes functions to change the color of the light on the SPIKE Prime hub.To use the Light module add the following import statement to your project:
```python
from hub import light
```
All functions in the module should be called inside the `light` module as a prefix like so:
```python
light.color(color.RED)
```

#### Functions

#### `color`
`color(light: int, color: int) -> None`
Change the color of a light on the hub.
```python
from hub import light
import color

# Change the light to red 
light.color(light.POWER, color.RED)
```

##### Parameters
----------
##### `light: int`
The light on the hub
##### `color: int`
A color from the `color` module
#### Constants
----------
#### `hub.light` Constants
`POWER` = 0
The power button. On SPIKE Prime it's the button between the left and right buttons.
`CONNECT`  = 1
The light around the Bluetooth connect button on SPIKE Prime.
### Light Matrix
To use the Light Matrix module add the following import statement to your project:
```python
from hub import light_matrix
```
All functions in the module should be called inside the `light_matrix` module as a prefix like so:
```python
light_matrix.write("Hello World")
```

#### Functions

#### `clear`
`clear() -> None`
Switches off all of the pixels on the Light Matrix.
```python
from hub import light_matrix
import time
# Update pixels to show an image on Light Matrix, and then turn them off using the clear function 

# Show a small heart 
light_matrix.show_image(2)

# Wait for two seconds 
time.sleep_ms(2000)

# Switch off the heart 
light_matrix.clear()
```

##### Parameters
----------
#### `get_orientation`
`get_orientation() -> int`
Retrieve the current orientation of the Light Matrix. 
 Can be used with the following constants: `orientation.UP`, `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`
##### Parameters
----------
#### `get_pixel`
`get_pixel(x: int, y: int) -> int`
Retrieve the intensity of a specific pixel on the Light Matrix.
```python
from hub import light_matrix

# Show a heart 
light_matrix.show_image(1)

# Print the value of the center pixel's intensity 
print(light_matrix.get_pixel(2, 2))

```

##### Parameters
----------
##### `x: int`
The X value, range (0 - 4)
##### `y: int`
The Y value, range (0 - 4)
#### `set_orientation`
`set_orientation(top: int) -> int`
Change the orientation of the Light Matrix. All subsequent calls will use the new orientation.
 Can be used with the following constants: `orientation.UP`, `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`
##### Parameters
----------
##### `top: int`
The side of the hub to be the top
#### `set_pixel`
`set_pixel(x: int, y: int, intensity: int) -> None`
Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.
```python
from hub import light_matrix
# Turn on the pixel in the center of the hub 
light_matrix.set_pixel(2, 2, 100)
```

##### Parameters
----------
##### `x: int`
The X value, range (0 - 4)
##### `y: int`
The Y value, range (0 - 4)
##### `intensity: int`
How bright to light up the pixel
#### `show`
`show(pixels: list[int]) -> None`
Change all the lights at the same time.
```python
from hub import light_matrix
# Update all pixels on Light Matrix using the show function 

# Create a list with 25 identical intensity values 
pixels = [100] * 25 

# Update all pixels to show same intensity 
light_matrix.show(pixels)
```

##### Parameters
----------
##### `pixels: Iterable`
A list containing light intensity values for all 25 pixels.
#### `show_image`
`show_image(image: int) -> None`
Display one of the built in images on the display.
```python
from hub import light_matrix
# Update pixels to show an image on Light Matrix using the show_image function 

# Show a smiling face 
light_matrix.show_image(light_matrix.IMAGE_HAPPY)
```

##### Parameters
----------
##### `image: int`
The id of the image to show. The range of available images is 1 to 67. There are consts on the `light_matrix` module for these.
#### `write`
`write(text: str, intensity: int = 100, time_per_character: int = 500) -> Awaitable`
Displays text on the Light Matrix, one letter at a time, scrolling from right to left except if there is a single character to show which will not scroll
```python
from hub import light_matrix
# White a message to the hub 
light_matrix.write("Hello, world!")
```

##### Parameters
----------
##### `text: str`
The text to display
##### `intensity: int`
How bright to light up the pixel
##### `time_per_character: int`
How long to show each character on the display
#### Constants
----------
#### `hub.light_matrix` Constants
`IMAGE_HEART` = 1

`IMAGE_HEART_SMALL` = 2

`IMAGE_HAPPY` = 3

`IMAGE_SMILE` = 4

`IMAGE_SAD` = 5

`IMAGE_CONFUSED` = 6

`IMAGE_ANGRY` = 7

`IMAGE_ASLEEP` = 8

`IMAGE_SURPRISED` = 9

`IMAGE_SILLY` = 10

`IMAGE_FABULOUS` = 11

`IMAGE_MEH` = 12

`IMAGE_YES` = 13

`IMAGE_NO` = 14

`IMAGE_CLOCK12` = 15

`IMAGE_CLOCK1` = 16

`IMAGE_CLOCK2` = 17

`IMAGE_CLOCK3` = 18

`IMAGE_CLOCK4` = 19

`IMAGE_CLOCK5` = 20

`IMAGE_CLOCK6` = 21

`IMAGE_CLOCK7` = 22

`IMAGE_CLOCK8` = 23

`IMAGE_CLOCK9` = 24

`IMAGE_CLOCK10` = 25

`IMAGE_CLOCK11` = 26

`IMAGE_ARROW_N` = 27

`IMAGE_ARROW_NE` = 28

`IMAGE_ARROW_E` = 29

`IMAGE_ARROW_SE` = 30

`IMAGE_ARROW_S` = 31

`IMAGE_ARROW_SW` = 32

`IMAGE_ARROW_W` = 33

`IMAGE_ARROW_NW` = 34

`IMAGE_GO_RIGHT` = 35

`IMAGE_GO_LEFT` = 36

`IMAGE_GO_UP` = 37

`IMAGE_GO_DOWN` = 38

`IMAGE_TRIANGLE` = 39

`IMAGE_TRIANGLE_LEFT` = 40

`IMAGE_CHESSBOARD` = 41

`IMAGE_DIAMOND` = 42

`IMAGE_DIAMOND_SMALL` = 43

`IMAGE_SQUARE` = 44

`IMAGE_SQUARE_SMALL` = 45

`IMAGE_RABBIT` = 46

`IMAGE_COW` = 47

`IMAGE_MUSIC_CROTCHET` = 48

`IMAGE_MUSIC_QUAVER` = 49

`IMAGE_MUSIC_QUAVERS` = 50

`IMAGE_PITCHFORK` = 51

`IMAGE_XMAS` = 52

`IMAGE_PACMAN` = 53

`IMAGE_TARGET` = 54

`IMAGE_TSHIRT` = 55

`IMAGE_ROLLERSKATE` = 56

`IMAGE_DUCK` = 57

`IMAGE_HOUSE` = 58

`IMAGE_TORTOISE` = 59

`IMAGE_BUTTERFLY` = 60

`IMAGE_STICKFIGURE` = 61

`IMAGE_GHOST` = 62

`IMAGE_SWORD` = 63

`IMAGE_GIRAFFE` = 64

`IMAGE_SKULL` = 65

`IMAGE_UMBRELLA` = 66

`IMAGE_SNAKE` = 67

### Motion Sensor
To use the Motion Sensor module add the following import statement to your project:
```python
from hub import motion_sensor
```
All functions in the module should be called inside the `motion_sensor` module as a prefix like so:
```python
motion_sensor.up_face()
```

#### Functions

#### `acceleration`
`acceleration(raw_unfiltered: bool) -> tuple[int, int, int]`
Returns a tuple containing x, y & z acceleration values as integers. The values are mili G, so 1 / 1000 G
##### Parameters
----------
##### `raw_unfiltered: bool`
If we want the data back raw and unfiltered
#### `angular_velocity`
`angular_velocity(raw_unfiltered: bool) -> tuple[int, int, int]`
Returns a tuple containing x, y & z angular velocity values as integers. The values are decidegrees per second
##### Parameters
----------
##### `raw_unfiltered: bool`
If we want the data back raw and unfiltered
#### `gesture`
`gesture() -> int`
Returns the gesture recognized.

Possible values are:

`motion_sensor.TAPPED`
`motion_sensor.DOUBLE_TAPPED`
`motion_sensor.SHAKEN`
`motion_sensor.FALLING`
`motion_sensor.UNKNOWN`
##### Parameters
----------
#### `get_yaw_face`
`get_yaw_face() -> int`
Retrieve the face of the hub that yaw is relative to.
If you put the hub on a flat surface with the face returned pointing up, when you rotate the hub only the yaw will update
`motion_sensor.TOP` The SPIKE Prime hub face with the USB charging port.
`motion_sensor.FRONT` The SPIKE Prime hub face with the Light Matrix.
`motion_sensor.RIGHT` The right side of the SPIKE Prime hub when facing the front hub face.
`motion_sensor.BOTTOM` The side of the SPIKE Prime hub where the battery is.
`motion_sensor.BACK` The SPIKE Prime hub face where the speaker is.
`motion_sensor.LEFT` The left side of the SPIKE Prime hub when facing the front hub face.
##### Parameters
----------
#### `quaternion`
`quaternion() -> tuple[float, float, float, float]`
Returns the hub orientation quaternion as a `tuple[w: float, x: float, y: float, z: float]`.
##### Parameters
----------
#### `reset_tap_count`
`reset_tap_count() -> None`
Reset the tap count returned by the `tap_count` function
##### Parameters
----------
#### `reset_yaw`
`reset_yaw(angle: int) -> None`
Change the yaw angle offset.
The angle set will be the new yaw value.
##### Parameters
----------
##### `angle: int`

#### `set_yaw_face`
`set_yaw_face(up: int) -> bool`
Change what hub face is used as the yaw face.If you put the hub on a flat surface with this face pointing up, when you rotate the hub only the yaw will update
##### Parameters
----------
##### `up: int`
The hub face that should be set as the upwards facing hub face.
Available values are:

`motion_sensor.TOP` The SPIKE Prime hub face with the USB charging port.
`motion_sensor.FRONT` The SPIKE Prime hub face with the Light Matrix.
`motion_sensor.RIGHT` The right side of the SPIKE Prime hub when facing the front hub face.
`motion_sensor.BOTTOM` The side of the SPIKE Prime hub where the battery is.
`motion_sensor.BACK` The SPIKE Prime hub face where the speaker is.
`motion_sensor.LEFT` The left side of the SPIKE Prime hub when facing the front hub face.
#### `stable`
`stable() -> bool`
Whether or not the hub is resting flat.
##### Parameters
----------
#### `tap_count`
`tap_count() -> int`
Returns the number of taps recognized since the program started or last time `motion_sensor.reset_tap_count()` was called.
##### Parameters
----------
#### `tilt_angles`
`tilt_angles() -> tuple[int, int, int]`
Returns a tuple containing yaw pitch and roll values as integers. Values are decidegrees
##### Parameters
----------
#### `up_face`
`up_face() -> int`
Returns the Hub face that is currently facing up
`motion_sensor.TOP` The SPIKE Prime hub face with the USB charging port.
`motion_sensor.FRONT` The SPIKE Prime hub face with the Light Matrix.
`motion_sensor.RIGHT` The right side of the SPIKE Prime hub when facing the front hub face.
`motion_sensor.BOTTOM` The side of the SPIKE Prime hub where the battery is.
`motion_sensor.BACK` The SPIKE Prime hub face where the speaker is.
`motion_sensor.LEFT` The left side of the SPIKE Prime hub when facing the front hub face.
##### Parameters
----------
#### Constants
----------
#### `hub.motion_sensor` Constants
`TAPPED` = 0

`DOUBLE_TAPPED` = 1

`SHAKEN` = 2

`FALLING` = 3

`UNKNOWN` = -1

`TOP` = 0
The SPIKE Prime hub face with the Light Matrix.
`FRONT` = 1
The SPIKE Prime hub face where the speaker is.
`RIGHT` = 2
The right side of the SPIKE Prime hub when facing the front hub face.
`BOTTOM` = 3
The side of the SPIKE Prime hub where the battery is.
`BACK` = 4
The SPIKE Prime hub face with the USB charging port.
`LEFT` = 5
The left side of the SPIKE Prime hub when facing the front hub face.
### Port
This module contains constants that enables easy access to the ports on the SPIKE Prime hub. Use the constants in all functions that takes a `port` parameter.To use the Port module add the following import statement to your project:
```python
from hub import port
```
All functions in the module should be called inside the `port` module as a prefix like so:
```python
port.A
```

#### Constants
----------
#### `hub.port` Constants
`A` = 0
The Port that is labelled ‘A’ on the Hub.
`B` = 1
The Port that is labelled ‘B’ on the Hub.
`C` = 2
The Port that is labelled ‘C’ on the Hub.
`D` = 3
The Port that is labelled ‘D’ on the Hub.
`E` = 4
The Port that is labelled ‘E’ on the Hub.
`F` = 5
The Port that is labelled ‘F’ on the Hub.
### Sound
To use the Sound module add the following import statement to your project:
```python
from hub import sound
```
All functions in the module should be called inside the `sound` module as a prefix like so:
```python
sound.stop()
```

#### Functions

#### `beep`
`beep(freq: int = 440, duration: int = 500, volume: int = 100, *, attack: int = 0, decay: int = 0, sustain: int = 100, release: int = 0, transition: int = 10, waveform: int = WAVEFORM_SINE, channel: int = DEFAULT) -> Awaitable`
Plays a beep sound from the hub
##### Parameters
----------
##### `freq: int`
The frequency to play
##### `duration: int`
The duration in milliseconds
##### `volume: int`
The volume (0-100)
##### Optional keyword arguments:

##### `attack: int`
The time taken for initial run-up of level from nil to peak, beginning when the key is pressed.
##### `decay: int`
The time taken for the subsequent run down from the attack level to the designated sustain level.
##### `sustain: int`
The level during the main sequence of the sound's duration, until the key is released.
##### `release: int`
The time taken for the level to decay from the sustain level to zero after the key is released
##### `transition: int`
time in milliseconds to transition into the sound if something is already playing in the channel
##### `waveform: int`
The synthesized waveform. Use one of the constants in the `hub.sound` module.
##### `channel: int`
The desired channel to play on, options are `sound.DEFAULT` and `sound.ANY`
#### `stop`
`stop() -> None`
Stops all noise from the hub
##### Parameters
----------
#### `volume`
`volume(volume: int) -> None`

##### Parameters
----------
##### `volume: int`
The volume (0-100)
#### Constants
----------
#### `hub.sound` Constants
`ANY` = -2

`DEFAULT` = -1

`WAVEFORM_SINE` = 1

`WAVEFORM_SAWTOOTH` = 3

`WAVEFORM_SQUARE` = 2

`WAVEFORM_TRIANGLE` = 1

### Functions

### `device_uuid`
`device_uuid() -> str`
Retrieve the device id.
#### Parameters
----------
### `hardware_id`
`hardware_id() -> str`
Retrieve the hardware id.
#### Parameters
----------
### `power_off`
`power_off() -> int`
Turns off the hub.
#### Parameters
----------
### `temperature`
`temperature() -> int`
Retrieve the hub temperature. Measured in decidegrees celsius (d°C) which is 1 / 10 of a degree celsius (°C)
#### Parameters
----------
## Motor
To use a Motor add the following import statement to your project:
```python
import motor
```
All functions in the module should be called inside the `motor` module as a prefix like so:
```python
motor.run(port.A, 1000)
```

### Functions

### `absolute_position`
`absolute_position(port: int) -> int`
Get the absolute position of a Motor
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `get_duty_cycle`
`get_duty_cycle(port: int) -> int`
Get the pwm of a Motor
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `relative_position`
`relative_position(port: int) -> int`
Get the relative position of a Motor
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### `reset_relative_position`
`reset_relative_position(port: int, position: int) -> None`
Change the position used as the offset when using the `run_to_relative_position` function.
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `position: int`
The degree of the motor
### `run`
`run(port: int, velocity: int, *, acceleration: int = 1000) -> None`
Start a Motor at a constant speed
```python
from hub import port
import motor, time

# Start motor 
motor.run(port.A, 1000)

```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### Optional keyword arguments:

#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
### `run_for_degrees`
`run_for_degrees(port: int, degrees: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Turn a motor for a specific number of degrees
When awaited returns a status of the movement that corresponds to one of the following constants:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.CANCELED`
`motor.ERROR`
`motor.DISCONNECTED`
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `degrees: int`
The number of degrees
#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### Optional keyword arguments:

#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `run_for_time`
`run_for_time(port: int, duration: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Run a Motor for a limited amount of time
When awaited returns a status of the movement that corresponds to one of the following constants:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.ERROR`
`motor.DISCONNECTED`
```python
from hub import port
import runloop
import motor

async def main():
    # Run at 1000 velocity for 1 second 
    await motor.run_for_time(port.A, 1000, 1000)

    # Run at 280 velocity for 1 second 
    await motor_pair.run_for_time(port.A, 1000, 280)

    # Run at 280 velocity for 10 seconds with a slow deceleration 
    await motor_pair.run_for_time(port.A, 10000, 280, deceleration=10)

runloop.run(main())
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `duration: int`
The duration in milliseconds
#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### Optional keyword arguments:

#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `run_to_absolute_position`
`run_to_absolute_position(port: int, position: int, velocity: int, *, direction: int = motor.SHORTEST_PATH, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Turn a motor to an absolute position.
When awaited returns a status of the movement that corresponds to one of the following constants:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.CANCELED`
`motor.ERROR`
`motor.DISCONNECTED`
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `position: int`
The degree of the motor
#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### Optional keyword arguments:

#### `direction: int`
The direction to turn.
Options are:

 `motor.CLOCKWISE`
`motor.COUNTERCLOCKWISE`
`motor.SHORTEST_PATH`
`motor.LONGEST_PATH`
#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `run_to_relative_position`
`run_to_relative_position(port: int, position: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Turn a motor to a position relative to the current position.
When awaited returns a status of the movement that corresponds to one of the following constants:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.CANCELED`
`motor.ERROR`
`motor.DISCONNECTED`
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `position: int`
The degree of the motor
#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### Optional keyword arguments:

#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `set_duty_cycle`
`set_duty_cycle(port: int, pwm: int) -> None`
Start a Motor with a specific pwm
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### `pwm: int`
The PWM value (-10000-10000)
### `stop`
`stop(port: int, *, stop: int = BRAKE) -> None`
Stops a motor
```python
from hub import port
import motor, time

# Start motor 
motor.run(port.A, 1000)

# Wait for 2 seconds 
time.sleep_ms(2000)

# Stop motor 
motor.stop(port.A)
```

#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
#### Optional keyword arguments:

#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
### `velocity`
`velocity(port: int) -> int`
Get the velocity (deg/sec) of a Motor
#### Parameters
----------
#### `port: int`
A port from the `port` submodule in the `hub` module
### Constants
----------
### `motor` Constants
`READY` = 0

`RUNNING` = 1

`STALLED` = 2

`CANCELLED` = 3

`ERROR` = 4

`DISCONNECTED` = 5

`COAST` = 0

`BRAKE` = 1

`HOLD` = 2

`CONTINUE` = 3

`SMART_COAST` = 4

`SMART_BRAKE` = 5

`CLOCKWISE` = 0

`COUNTERCLOCKWISE` = 1

`SHORTEST_PATH` = 2

`LONGEST_PATH` = 3

## Motor Pair
The `motor_pair` module is used to run motors in a synchronized fashion. This mode is optimal for creating drivebases where you'd want a pair of motors to start and stop at the same time.To use the `motor_pair` module simply import the module like so:
```python
import motor_pair
```
All functions in the module should be called inside the `motor_pair` module as a prefix like so:
```python
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
```

### Functions

### `move`
`move(pair: int, steering: int, *, velocity: int = 360, acceleration: int = 1000) -> None`
Move a Motor Pair at a constant speed until a new command is given.
```python
from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    await runloop.sleep_ms(2000)

    # Move straight at default velocity 
    motor_pair.move(motor_pair.PAIR_1, 0)

    await runloop.sleep_ms(2000)

    # Move straight at a specific velocity 
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)

    await runloop.sleep_ms(2000)

    # Move straight at a specific velocity and acceleration 
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=280, acceleration=100)

runloop.run(main())
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### `steering: int`
The steering (-100 to 100)
#### Optional keyword arguments:

#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
### `move_for_degrees`
`move_for_degrees(pair: int, degrees: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Move a Motor Pair at a constant speed for a specific number of degrees.
When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.CANCELED`
`motor.ERROR`
`motor.DISCONNECTED`
```python
from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight at default velocity for 90 degrees 
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0)

    # Move straight at a specific velocity 
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=280)

    # Move straight at a specific velocity with a slow deceleration 
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=280, deceleration=10)

runloop.run(main())
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### `degrees: int`
The number of degrees
#### `steering: int`
The steering (-100 to 100)
#### Optional keyword arguments:

#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `move_for_time`
`move_for_time(pair: int, duration: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Move a Motor Pair at a constant speed for a specific duration.
When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.CANCELED`
`motor.ERROR`
`motor.DISCONNECTED`
```python
from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight at default velocity for 1 second 
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0)

    # Move straight at a specific velocity for 1 second 
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0, velocity=280)

    # Move straight at a specific velocity for 10 seconds with a slow deceleration 
    await motor_pair.move_for_time(motor_pair.PAIR_1, 10000, 0, velocity=280, deceleration=10)

runloop.run(main())
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### `duration: int`
The duration in milliseconds
#### `steering: int`
The steering (-100 to 100)
#### Optional keyword arguments:

#### `velocity: int`
The velocity in degrees/sec

Value ranges depends on motor type.

Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `move_tank`
`move_tank(pair: int, left_velocity: int, right_velocity: int, *, acceleration: int = 1000) -> None`
Perform a tank move on a Motor Pair at a constant speed until a new command is given.
```python
from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight at default velocity 
    motor_pair.move_tank(motor_pair.PAIR_1, 1000, 1000)

    await runloop.sleep_ms(2000)

    # Turn right 
    motor_pair.move_tank(motor_pair.PAIR_1, 0, 1000)

    await runloop.sleep_ms(2000)

    # Perform tank turn 
    motor_pair.move_tank(motor_pair.PAIR_1, 1000, -1000)

runloop.run(main())
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### `left_velocity: int`
The velocity (deg/sec) of the left motor.
#### `right_velocity: int`
The velocity (deg/sec) of the right motor.
#### Optional keyword arguments:

#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
### `move_tank_for_degrees`
`move_tank_for_degrees(pair: int, degrees: int, left_velocity: int, right_velocity: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Perform a tank move on a Motor Pair at a constant speed until a new command is given.
When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.CANCELED`
`motor.ERROR`
`motor.DISCONNECTED`
```python
from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight at default velocity for 360 degrees 
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 1000, 1000)

    # Turn right for 180 degrees 
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 0, 1000)

    # Perform tank turn for 720 degrees 
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 720, 1000, -1000)

runloop.run(main())
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### `degrees: int`
The number of degrees
#### `left_velocity: int`
The velocity (deg/sec) of the left motor.
#### `right_velocity: int`
The velocity (deg/sec) of the right motor.
#### Optional keyword arguments:

#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `move_tank_for_time`
`move_tank_for_time(pair: int, left_velocity: int, right_velocity: int, duration: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable`
Perform a tank move on a Motor Pair at a constant speed for a specific amount of time.
When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:

`motor.READY`
`motor.RUNNING`
`motor.STALLED`
`motor.CANCELED`
`motor.ERROR`
`motor.DISCONNECTED`
```python
from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight at default velocity for 1 second 
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, 1000, 1000)

    # Turn right for 3 seconds 
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 1000, 3000)

    # Perform tank turn for 2 seconds 
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, -1000, 2000)

runloop.run(main())
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### `duration: int`
The duration in milliseconds
#### `left_velocity: int`
The velocity (deg/sec) of the left motor.
#### `right_velocity: int`
The velocity (deg/sec) of the right motor.
#### Optional keyword arguments:

#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
#### `acceleration: int`
The acceleration (deg/sec²) (1 - 10000)
#### `deceleration: int`
The deceleration (deg/sec²) (1 - 10000)
### `pair`
`pair(pair: int, left_motor: int, right_motor: int) -> None`
pair two motors (`left_motor` & `right_motor`) and store the paired motors in `pair`. 
Use `pair` in all subsequent `motor_pair` related function calls.
```python
import motor_pair
from hub import port

motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### `left_motor: int`
The port of the left motor. Use the `port` submodule in the `hub` module.
#### `right_motor: int`
The port of the right motor. Use the `port` submodule in the `hub` module.
### `stop`
`stop(pair: int, *, stop: int = motor.BRAKE) -> None`
Stops a Motor Pair.
```python
import motor_pair

motor_pair.stop(motor_pair.PAIR_1)
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
#### Optional keyword arguments:

#### `stop: int`
The behavior of the Motor after it has stopped. Use the constants in the `motor` module.

Possible values are
`motor.COAST` to make the motor coast until a stop
`motor.BREAK` to brake and continue to brake after stop
`motor.HOLD` to tell the motor to hold it's position
`motor.CONTINUE` to tell the motor to keep running at whatever velocity it's running at until it gets another command
`motor.SMART_COAST` to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
`motor.SMART_BRAKE` to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command
### `unpair`
`unpair(pair: int) -> None`
Unpair a Motor Pair.
```python
import motor_pair

motor_pair.unpair(motor_pair.PAIR_1)
```

#### Parameters
----------
#### `pair: int`
The pair slot of the Motor Pair.
### Constants
----------
### `motor_pair` Constants
`PAIR_1` = 0
First Motor Pair
`PAIR_2` = 1
Second Motor Pair
`PAIR_3` = 2
Third Motor Pair
## Orientation
The `orientation` module contains all the orientation constants to use with the `light_matrix` module.To use the orientation module add the following import statement to your project:
```python
import orientation
```

### Constants
----------
### `orientation` Constants
`UP` = 0

`RIGHT` = 1

`DOWN` = 2

`LEFT` = 3

## Runloop
The `runloop` module contains all functions and constants to use the Runloop.

To use the Runloop module add the following import statement to your project:
```python
import runloop
```
All functions in the module should be called inside the `runloop` module as a prefix like so:
```python
runloop.run(some_async_function())
```

### Functions

### `run`
`run(*functions: Awaitable) -> None`
Start any number of parallel `async` functions. This is the function you should use to create programs with a similar structure to Word Blocks.
#### Parameters
----------
#### *functions: awaitable
The functions to run
### `sleep_ms`
`sleep_ms(duration: int) -> Awaitable`
Pause the execution of the application for any amount of milliseconds.
```python
from hub import light_matrix
import runloop

async def main():
    light_matrix.write("Hi!")
    # Wait for ten seconds 
    await runloop.sleep_ms(10000)
    light_matrix.write("Are you still here?")

runloop.run(main())

```

#### Parameters
----------
#### `duration: int`
The duration in milliseconds
### `until`
`until(function: Callable[[], bool], timeout: int = 0) -> Awaitable`
Returns an awaitable that will return when the condition in the function or lambda passed is `True` or when it times out
```python
import color_sensor
import color
from hub import port
import runloop

def is_color_red():
    return color_sensor.color(port.A) is color.RED

async def main():
    # Wait until Color Sensor sees red 
    await runloop.until(is_color_red)
    print("Red!")

runloop.run(main())

```

#### Parameters
----------
#### function: Callable[[], bool]
A callable with no parameters that returns either `True` or `False`.
Callable is anything that can be called, so a `def` or a `lambda`
#### `timeout: int`
A timeout for the function in milliseconds.
If the callable does not return `True` within the timeout, the `until` still resolves after the timeout.
0 means no timeout, in that case it will not resolve until the callable returns `True`
# Legal Documents

## Terms of Use
Introduction
------------

This license for the LEGO® Education SPIKE™ Software (hereinafter the "App") is granted by LEGO System A/S, Aastvej 1, DK-7190 Billund, Denmark, CVR no. 47 45 87 14. The LEGO Group and any and all entities that control, are controlled by or are affiliated or under common control with the LEGO Group or LEGO System A/S are collectively referred to here in as “we”, “us,” or “our”. We provide certain third-party software subject to separate license terms either presented at the time of installation or otherwise provided with the App (“Third-Party Software”). Such Third-Party Software is not included in the meaning of the term “App.” By downloading or using the App or by clicking a box that states that you accept or agree to these Terms and Conditions, you acknowledge that you have read and understand these Terms and Conditions and signify your agreement to be bound by the terms set out herein. If you do not agree to the Terms and Conditions, you may not use the App. The App is distributed by us via several outlet partners, including via the Apple App Store, Google Play Store, Microsoft Windows store, and the LEGOeducation.com website. If you have obtained the App from any other source, it may be defective or significantly revised from the original product. Use of any modified version is at your own risk and we do not assume any liability in that respect. For U.S.: LEGO Brand Retail Inc. doing business as LEGO Education North America, 501 Boylston Street Suite 4103, Boston, Massachusetts, 02116. E-mail: orders@LEGOeducation.us For the rest of the world: LEGO Systems A/S doing business as LEGO Education International, Aastvej 1, DK-7190 Billund, Denmark. E-mail: customer.service@LEGOeducation.comProcessing of Personal Information and Use of Cookies
-----------------------------------------------------

Our [Privacy Policy][1] and [Cookie Policy][2] are an integrated part of these Terms and Conditions. For information on the processing of personal information collected online from children, please refer to our Privacy Policy. In respect of LEGO Education SPIKE, the LEGO Group may collect aggregated data relating to the use of a product to help improve product performance and offerings. However, the LEGO Group will not under any circumstances collect any personal data relating to individual users (including any teacher or student) through LEGO Education SPIKE. (LEGO Education is a business division within the LEGO Group and is responsible for the product and solution lines offered under the “LEGO Education” brand.) Any third parties acting on behalf of the LEGO Group are bound by the same rules and principles as the LEGO Group.


  [1]: http://www.lego.com/legal/legal-notice/privacy-policy-full
  [2]: http://www.lego.com/legal/cookieinfoUse of Content
-------

No rights are granted to you other than a non-exclusive, limited license to use the App on the terms expressly set forth in these Terms and Conditions, including any right to any enhancement or update. All information, materials, functions, and other content ("Content") contained in the App are our copyrighted property or the copyrighted property of our licensors or licensees. All trademarks, service marks, trade names, and trade dresses are proprietary to us and/or our licensors or licensees. We may terminate your further access to the App, change the App, or delete content or features in any way, at any time and for any or no reason. You may only use the App (a) to carry out non-commercial projects that involve the LEGO Education SPIKE; or (b) to, for non-commercial purposes, create content through activities described in (a) above. You may NOT: (1) permit other individuals or entities to use the App, unless you ensure that the other individuals or entities (a) understand that their use of the App is subject to the terms and conditions of these Terms and Conditions, and (b) agree to and comply with these Terms and Conditions; (2) reverse engineer, decompile, disassemble, or otherwise reduce the App or Content to a human-perceivable form (except to the extent that this restriction is expressly prohibited by law); modify or translate the App or Content; or create derivative works based upon the App or Content; (3) copy the App or Content (except for back-up purposes); (4) sell, resell, rent, lease, assign, distribute, or otherwise transfer the App or Content, or any of the licensed rights with respect to the App or Content; (5) transmit the App or Content on the Internet; (6) use the back-up copy other than as a replacement for the primary copy; (7) use the App for any commercial purpose; (8) remove any proprietary notices or labels in or on the App or Content; (9) use the App for any purpose related to the manufacture, marketing, sale, or distribution of plastic building bricks; (10) use the App to gain access to unencrypted data in a manner that defeats the digital content protection provided in the App, or use the App in an attempt to, or in conjunction with any device, program or service designed to, circumvent technological measures employed to control access to, or the rights in, a content file or other work protected by the copyright laws of any jurisdiction; (11) take any action that results in any part of the App being subject to a license that requires, or purports to require, as a condition of use, modification or distribution, that (a) any code that is or could become subject to the license be disclosed or distributed in source code form, or (b) others have the right to modify or create derivative works of any code that is or could become subject to the license; or (12) directly or indirectly export, re-export, download, transmit, or transfer the App in violation of any provision within these Terms and Conditions. Any use or transfer of the App or Content in violation of the above will lead to immediate, automatic termination of your license.Title
-------

All title, ownership, rights, and intellectual property rights in and to the App and Content, including the text, building instructions, and images within the App, and all copies hereof, shall remain with us and/or our suppliers and licensors. All rights not expressly granted to you under these Terms and Conditions are reserved to us and/or our suppliers and licensors. The App and all Content is protected by national copyright laws and international copyright treaties. LEGO, the LEGO logo, the Minifigure and the LEGO Education SPIKE logo are trademarks and/or copyrights of the LEGO Group. ©2019-2023 The LEGO Group. All rights reserved. For notices and licenses relating to Third-Party Software, please see the following file Licenses.Accounts
--------

Some services on the App may permit or require you to create a LEGO ID account to participate or to secure additional benefits. Please see the Terms and Conditions for LEGO ID [here][1]. We may suspend or terminate your ability to use the App or portion hereof in case of failure to comply with said Terms and Conditions for LEGO ID or any special terms related to a particular service.


  [1]: https://identity.lego.com/en-US/termsApp Distributors/Stores
-----------------------

You acknowledge that these Terms and Conditions are concluded between you and us only, and not with app distributers / stores, e.g. Apple, Inc., Google, Amazon, Samsung etc. (“App Distributors”). We, and not the App Distributers, are solely responsible for the App and the services and Content available therein. The parties agree that the App Distributors have no obligation to provide maintenance or support services with respect to the App. To the maximum extent permitted by applicable law, the App Distributors will have no warranty obligation whatsoever with respect to the App. You agree that we, and not the App Distributors, are responsible for addressing any claims by you or any third party relating to the App or your possession and/or use of the App, including, but not limited to: (i) product liability claims; (ii) any claim that the App fails to conform to any applicable legal or regulatory requirement; and (iii) claims arising under consumer protection or similar legislation. You agree that we, and not the App Distributors, are responsible for the investigation, defense, settlement, and discharge of any third party intellectual property infringement claim related to the App or your possession and use of the App. You represent and warrant that (i) you are not located in a country that is subject to a U.S. Government embargo, or that has been designated by the U.S. Government as a "terrorist supporting" country; and (ii) you are not listed on any U.S. Government list of prohibited or restricted parties. You agree to comply with all applicable third party terms of agreement when using the App (e.g. you must not be in violation of your wireless data service terms of agreement when using the App). The parties agree that the App Distributors and their subsidiaries are third party beneficiaries to these Terms and Conditions. Upon your acceptance of the Terms and Conditions, the App Distributors will have the right (and will be deemed to have accepted the right) to enforce the Terms and Conditions against you as third party beneficiaries thereof. You agree that your use of the App is subject to the usage rules set forth in the App Distributor’s then-current terms of service for downloading apps through the App Distributor.Indemnification
-------

You are responsible for maintaining the confidentiality of your username(s), password(s), and your account(s), as well as all activities that occur under your account(s). To the extent possible under applicable law, you hereby agree to indemnify, defend, and hold us, our licensors, licensees, distributors, agents, representatives, and other authorized users, and each of the foregoing entities' respective resellers, distributors, service providers, and suppliers, and all of the foregoing entities' respective officers, directors, owners, employees, agents, representatives and assigns (collectively the "Indemnified Parties") harmless from and against any and all losses, damages, liabilities, and costs (including settlement costs and any legal or other fees and expenses for investigating or defending any actions or threatened actions) incurred by the Indemnified Parties in connection with any claim arising out of any breach by you of these Terms and Conditions or claims arising from your use of the App and/or your account(s). You shall use your best efforts to cooperate with us in the defense of any claim. We reserve the right, at our own expense, to employ separate counsel and assume the exclusive defense and control of any matter otherwise subject to indemnification by you.No Warranty
-------

THE APP AND ALL THIRD-PARTY SOFTWARE IS PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, NON-INFRINGEMENT, OR ANY OTHER APPLICABLE STATUTORY WARRANTIES (TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW). THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE APP, AND THIRD-PARTY SOFTWARE, IS WITH YOU. SHOULD THE APP AND/OR THIRD-PARTY SOFTWARE PROVE DEFECTIVE, YOU (AND NOT THE LEGO GROUP OR ANY AUTHORIZED DEALER) ASSUME THE ENTIRE COST OF ALL NECESSARY SERVICING, REPAIR, OR CORRECTION. SOME STATES AND COUNTRIES DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO THE ABOVE EXCLUSION MAY NOT APPLY TO YOU. THE LEGO GROUP DOES NOT WARRANT THAT THE FUNCTIONALITY PROVIDED BY THE APP, THIRD-PARTY SOFTWARE, OR ANY PROJECTS BASED ON THE APP WILL MEET YOUR REQUIREMENTS OR THAT THE OPERATION OF THE APP, THIRD-PARTY SOFTWARE, AND SAID PROJECTS WILL BE UNINTERRUPTED OR ERROR FREE.Limitation of Liability
----------------------

IN NO EVENT WILL THE LEGO GROUP OR ANY OF ITS SUPPLIERS OR LICENSORS BE LIABLE TO YOUR FOR ANY DAMAGES, INCLUDING WITHOUT LIMITATION ANY LOST PROFITS, LOST SAVINGS OR OTHER INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF OR INABILITY TO USE THE APP OR ANY THIRD-PARTY SOFTWARE, EVEN IF THE LEGO GROUP, ANY OF ITS SUPPLIERS OR LICENSORS OR AN AUTHORIZED DEALER HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES; OR FOR ANY CLAIM BY ANY OTHER PARTY. THE LEGO GROUP’S SUPPLIERS AND LICENSORS MAKE NO WARRANTIES AND SHALL HAVE NO LIABILITY IN CONNECTION WITH THIS AGREEMENT. SOME COUNTRIES OR STATES DO NOT ALLOW THE LIMITATION OR EXCLUSION OF LIABILITY FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES SO THE ABOVE LIMITATION OR EXCLUSION MAY NOT APPLY TO YOU.Jurisdictional and Venue Issues
-------

These Terms and Conditions are governed by the laws of the country in which you acquired the license to the App. You acknowledge that the App is, and Third-Party Software provided with the App may be, subject to control under the export control laws and regulations of the United States of America and other countries and applicable global export control laws and regulations. You agree that you will not directly or indirectly export, re-export, transfer, download, or ship the App or any Third-Party Software via any means: (a) to any prohibited destination, entity or individual without the required export license(s) or authorization(s) from the United States Government and/or other applicable export licensing authority, or (b) in violation of the laws and regulations of the United States of America or the laws and regulations of the jurisdiction in which you use or are downloading the App or any Third-Party Software provided with the App. If you are downloading the App, you represent and warrant that: (a) you are not located in, or under the control of, any country or state the laws and regulations of which prohibit importation of the App or any Third-Party Software provided with the App; and (b) you are not located in, or under the control of, any country or state to which the laws and regulations of the United States of America and/or other applicable export control laws prohibit exportation of the App or any Third-Party Software provided with the App. If you are an agency, department, or other entity of the United States Government: (a) you are notified that the App is a "commercial item" developed exclusively at private expense, consisting of "commercial computer software" and "commercial computer software documentation" as such terms are defined or used in the applicable United States acquisition regulations; and (b) the App is licensed hereunder (i) only as a commercial item and (ii) with only those rights as are granted to all other licensees pursuant to the terms and conditions of these Terms and Conditions. You agree not to use, duplicate, or disclose the App in any way not expressly permitted by these Terms and Conditions. Nothing in these Terms and Conditions requires the LEGO Group or any of our suppliers or licensors to produce or furnish technical data for or to you. We make no representation that Content in the App, or any content of the Third-Party Software, is appropriate or available for use in any particular location. Those who choose to access the App do so on their own initiative and are responsible for compliance with all applicable laws including any applicable local laws.Severance
-------

If any term or provision within these Terms and Conditions is or becomes invalid, illegal, or unenforceable for any reason, this shall not affect the validity or enforceability of the remainder of these Terms and Conditions. In such event, the term or provision deemed to be invalid, illegal, or unenforceable shall be deemed modified to the minimum extent necessary to make it valid, legal, and enforceable.Amendment
-------

At any time, we may amend these Terms and Conditions (including by modification, deletion, and/or addition of any portion hereof). If we make a material amendment to these Terms and Conditions, we will notify you of such amendment by posting notice thereof on the website LEGOeducation.com/support or via the relevant app store or the App itself. Any such amendment to these Terms and Conditions will be effective thirty (30) calendar days following publication of the aforementioned notice. By using the App following the thirty (30) calendar days' notice, you consent to any material amendments.Termination
-------

This license and your right to use the App shall terminate automatically if you fail to comply with the provisions of these Terms and Conditions. No notice shall be required from us to effectuate such termination. Upon termination, you are obligated to immediately destroy all copies of the App and Content. The following sections of these Terms and Conditions shall survive any termination of this license: “Title,” “No Warranty,” “Limitation of Remedies,” “Jurisdictional and Venue Issues,” and “Termination.
## Cookies
We use cookies or similar technologies on our digital applications.
-------------------------------------------------------------------

Cookies and similar technologies are small data files that your browser or app set on your computer or device. When sent to our servers, this information can help us deliver a more user-friendly and properly functioning service.

Our applications collect some information (e.g. information on IP addresses, browsers, operating systems, date stamps and time stamps). This information will not be linked to any other information we collect about you unless you have consented to it. But not every cookie is the same. For a list of the categories of cookies we use, see below. 

The cookies and similar technologies we use fall into two categories.

Required Cookies: These cookies and similar technologies are required to enable core app functionality and are therefore always enabled. This category includes your IP address, selected country and language and, in the event an error occurs, your usage of the app when such error occurs. When such information is collected, we will not ask for your consent, because we have a legitimate purpose – to ensure core functionality. Please note that you can opt-out of the other categories, but you cannot opt-out from sending required information. 

Tracking of Non-Personal Information: The tracking of this information is optional and allows us to track your usage of our app for statistical purposes to optimize your experience. We only use this information where the purpose is considered legitimate and does not require consent. The information that we collect is limited to anonymous and aggregated information which does not include any personally identifiable information. We will not ask to get your permission to collect this information, however you can at any time opt out by clicking on the settings tab and then selecting the opt out feature.
## Cookies
We use cookies or similar technologies on our digital applications.
-------------------------------------------------------------------

We use cookies or similar technologies on our digital applications.

Cookies and similar technologies are small data files that your browser or app sets on your computer or device. When sent to our servers, this information can help us deliver a properly functioning service – for example, reporting errors when they occur.

Our applications collect some information (e.g. information on IP addresses, browsers, operating systems, date stamps and time stamps). This information will not be linked to any other information we collect about you unless you have consented to it, and our use of such information will be limited to facilitating online communication or processes that are strictly necessary for functionality (collectively, “Strictly Necessary Cookies”).

Strictly Necessary Cookies: These are required to enable core app functionality and are therefore always enabled. This category includes your IP address, selected country and language and, in the event an error occurs, this information will be also sent to our servers to help us resolve the error. When such information is collected, we will not ask for your consent, because we have a legitimate purpose – to ensure core functionality.
## Privacy
Our Privacy Policy
------------------

Welcome to our privacy policy! It’s great that you’d like to know more about how we keep your information safe. This policy will give you information about how we look after your personal data when you visit our website (regardless of where you visit it from) or use our services or our applications (apps). The policy also tells you about your privacy rights and how the law protects you. So, if you’re looking for more information on how we collect, store, use and share your personal data we collect, this is the place for you! Now to start us off with, a couple of practical but highly important details for you to take note of!
## Accessibility
Accessibility
-------
LEGO Education is committed to ensuring effective communication and digital accessibility to as many users as possible. We are continually improving the user experience for everyone, and apply the relevant accessibility standards to achieve these goals. We welcome your feedback on the accessibility of spike.LEGOEducation.com. Please let us know if you encounter accessibility barriers in accessing any area our website.
## Certificates

### TECHNIC Large Hub, Y
Model: HUB NO.6
#### South Africa
TA-2019/1047![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt11320c393316e8bf/627cbada79aed9366938091b/ICASA_logo.png)
### TECHNIC Large Hub, T
Model: HUB NO.6
#### South Africa
TA-2019/1047![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt11320c393316e8bf/627cbada79aed9366938091b/ICASA_logo.png)
### TECHNIC Small Hub
Model: HUB NO.7
#### South Africa
TA-2021/1706![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt11320c393316e8bf/627cbada79aed9366938091b/ICASA_logo.png)