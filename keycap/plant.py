import numpy as np
from .controller import Controller

class Plant:
    """
    A class representing a plant in a control system. The plant generates model values using a controller and 
    converts velocities to time values using a formula. The controller can be custom designed using the 
    `default_design_controller` method.
    """

    def __init__(self, controller=None):
        """
        Initialize the Plant with a Controller.

        Parameters:
        - Controller: The controller class for the keycap.
        """
        if (controller is None):
            self.controller = Controller()
        else:
            self.controller = controller

    def velocities_to_time(self, velocities):
        """
        Convert an array of velocities to time values using the formula: time = 1/velocity.
        This is the time pressed between each keypress.
        
        Parameters:
        - velocities (array-like): An array of velocity values.
        
        Returns:
        - (array-like): An array of time values.
        """
        return 1 / np.array(velocities)

    def generate_model(self, t):
        """
        Generate model values using the controller.

        Parameters:
        - t (array-like): Time series data.

        Returns:
        - (array-like): Model values.
        """
        velocities = self.controller.generate_model_values(t)
        return velocities

    def default_design_controller(self):
        """
        Default design the controller. You can expand on this with more sophisticated design logic.
        """
        self.controller.generate_D()
        self.controller.generate_alpha()
        self.controller.generate_w()
