import microbit

class MotoBitMotor:
    FORWARD_FLAG = 0x80

    def __init__(self, i2c_addr, cmd_speed, invert):
        self.i2c_addr = i2c_addr
        self.cmd_speed = cmd_speed
        self.invert = invert

    def __drive(self, speed):
        flags = 0
        if self.invert:
            speed = -speed
        if speed >= 0:
            flags |= MotoBitMotor.FORWARD_FLAG
        speed = int(speed / 100 * 127)
        if speed < -127:
            speed = -127
        if speed > 127:
            speed = 127
        speed = (speed & 0x7f) | flags
        microbit.i2c.write(self.i2c_addr, bytes([self.cmd_speed, speed]))

    def forward(self, speed):
        '''Forward motor control.

        Args:
            speed (int|float): -100 ~ +100
        '''
        self.__drive(speed)

    def reverse(self, speed):
        '''Reverse motor control.

        Args:
            speed (int|float): -100 ~ +100
        '''
        self.__drive(-speed)

class MotoBit:
    I2C_ADDR = 0x59
    CMD_ENABLE = 0x70
    CMD_SPEED_LEFT = 0x21
    CMD_SPEED_RIGHT = 0x20

    def enable(self):
        '''Enable motor driver.
        '''
        microbit.i2c.write(MotoBit.I2C_ADDR, bytes([MotoBit.CMD_ENABLE, 0x01]))

    def disable(self):
        '''Disable motor driver.
        '''
        microbit.i2c.write(MotoBit.I2C_ADDR, bytes([MotoBit.CMD_ENABLE, 0x00]))

    def left_motor(self, invert = False):
        '''Acquire left motor object.

        Args:
            invert (bool): Invert polarity. (default: False)
        '''
        return MotoBitMotor(MotoBit.I2C_ADDR, MotoBit.CMD_SPEED_LEFT, invert)

    def right_motor(self, invert = False):
        '''Acquire right motor object.

        Args:
            invert (bool): Invert polarity. (default: False)
        '''
        return MotoBitMotor(MotoBit.I2C_ADDR, MotoBit.CMD_SPEED_RIGHT, invert)
