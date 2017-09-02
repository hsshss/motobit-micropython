# Description

This module is SparkFun **moto:bit** driver for MicroPython.

# Usage

```python
motobit = MotoBit()

motobit.enable() # Enable motor driver

l = motobit.left_motor() # Acquire motor object
r = motobit.right_motor(invert=True) # Enable invert polarity

l.forward(100) # Forward motor control
r.reverse(50)  # Reverse motor control

l.forward(0) # Stop motor
r.forward(0)

l.forward(-100) # Reverse motor control
r.reverse(-50)  # Forward motor control

l.reverse(0) # Stop motor
r.reverse(0)

motobit.disable() # Disable motor driver
```

# License

These codes are licensed under CC0.

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](https://creativecommons.org/publicdomain/zero/1.0/deed)
