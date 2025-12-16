"""Controllers for both the driver and operator."""

import wpilib
from wpilib import RobotBase
from wpilib.simulation import PS4ControllerSim


class OurController(wpilib.XboxController):
    """A wrapper around wpilib.PS4Controller to provide easier access to common controls."""

    def getLeftStick(self) -> tuple[float, float]:
        """Get the position of the left stick as two values, both in the range [-1.0, 1.0].

        Note:
            Moving the stick to the right is +x, and down is +y.
        """
        return (self.getLeftX(), self.getLeftY())

    def getRightStick(self) -> tuple[float, float]:
        """Get the position of the right stick as two values, both in the range [-1.0, 1.0].

        Note:
            Moving the stick to the right is +x, and down is +y.
        """
        return (self.getRightX(), self.getRightY())

    def getLeftTriggerIsPressed(self) -> bool:
        """Checks if the left trigger is past a certain threshold (otherwise known as pressed)."""
        return self.getLeftTriggerAxis() > 0.5


class DriverController(OurController):
    """Controller with information focused on the driver controls.

    In simulation, keyboard input is supported via the simulation GUI.
    Drag "Keyboard 0" from System Joysticks to Joystick[0] in the sim GUI.

    Default keyboard mappings in sim GUI:
    - WASD: Left stick (strafe/forward-back)
    - Arrow keys or IJKL: Right stick (rotation)
    """

    def should_brake(self) -> bool:
        """Determine if the brake button is actively being pressed."""
        return self.getXButton()


class OperatorController(OurController):
    """Controller with information focused on the driver controls.

    In simulation, keyboard input is supported via the simulation GUI.
    Drag "Keyboard 0" from System Joysticks to Joystick[0] in the sim GUI.

    Default keyboard mappings in sim GUI:
    - WASD: Left stick (strafe/forward-back)
    - Arrow keys or IJKL: Right stick (rotation)
    """

    def should_intake(self) -> bool:
        """Determine whether or not the left bumper is pressed."""
        if self.getLeftBumperButton() and self.getLeftTriggerIsPressed():
            return False
        return self.getLeftBumperButton()

    def should_output(self) -> bool:
        """Determine whether or not the left trigger is pressed."""
        if self.getLeftBumperButton() and self.getLeftTriggerIsPressed():
            return False

        return self.getLeftTriggerIsPressed()
