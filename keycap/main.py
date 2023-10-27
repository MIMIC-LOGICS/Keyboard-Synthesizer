
from plant import Plant
from controller import Controller
from controller import ConfigurationManager
import numpy as np


if __name__ == "__main__":
    # Demonstration:

    controller = Controller()
    manager = ConfigurationManager()

    # Create a plant
    plant = Plant(controller)

    # Custom design the controller
    plant.default_design_controller()

    # Generate model values
    t = np.linspace(0, 1, 1000)
    velocities = plant.generate_model(t)

    # Convert velocities to time
    times = plant.velocities_to_time(velocities)

    print("Velocities: ", velocities)
    print("Times: ", times)