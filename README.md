# Keycap Equations for Human-Like and Synthetic Human Movements

The keycap equations model provides a method to generate human-like and synthetic human movements emulating the dynamics of keyboard typing. The system is comprised of a 'Plant', 'Controller', 'Keycap' functions, and a 'Configuration Manager'.

## Overview

The model is designed to capture the intricacies of human typing behaviors. As more samples are taken from the model, moving forward on the time axis, the velocity decreases due to the exponential terms in the model. 
To prevent the model from decaying too rapidly, time series are constrained to a range of 0-1 second with 1000 samples.

![Keycap](./assets/keycap.gif)

## Installation

```
pip install keycap
```

### Complexity and Variations

1. n:
General Description:The parameter `N` controls the complexity of the model. 
Practical Implication: With higher values of `N`, the model will present variations at different frequencies. Consequently, increasing `N` will also increase the velocity of the model. For optimal results, it's recommended to keep `N` between 500 and 5000. It's also beneficial to adjust the `N` value for individual users.
Frequency Domain Explanation: The number of Gaussian curves at different frequencies.

1. D (Amplitude):
General Description: Represents the amplitude of the keycap's response.
Practical Implication: The greater the value of D, the faster the keyboard writes.
Frequency Domain Explanation: In the context of a frequency domain representation, a larger D corresponds to a higher amplitude of the Gaussian function. It signifies a more dominant frequency component.

2. alpha (Damping Coefficient):
General Description: Captures the damping property of the keycap's response.
Practical Implication: Variation in alpha leads to variations in the velocity of the key response.
Frequency Domain Explanation: In frequency space, a greater value of alpha narrows the Gaussian function, making it more peaky. It's inversely proportional to the standard deviation of the Gaussian, indicating a more concentrated frequency component.

3. t (Time Variable):
General Description: This is the time variable, representing the progression of time in the simulation.
Practical Implication: The t values allow us to observe how the keycap response evolves over time. 

4. w (Frequency):
General Description: Determines the frequency characteristics of the keycap's response.
Practical Implication: The parameter w adds complexity to the key response. In simple terms, it can be thought of as controlling the "rhythm" of the keyboard writing pattern.
Frequency Domain Explanation: In frequency space, w dictates the position of Gaussian functions. A greater w means more the gaussian is more shifted to the right, representing a faster frequency component.

## Configuration

The model comes with the provision to load and save configurations, ensuring consistent characteristics across multiple sessions. The values generated within the same session, will have similar characteristics. The loading and saving of configurations is managed by the `Configuration Manager`.

## Classes Explained

### Plant

The `Plant` class represents a component in a control system. It's responsible for generating model values using a controller and converting velocities into time values.

- **velocities_to_time**: Converts an array of velocities to time values.
- **generate_model**: Produces model values utilizing the controller.
- **default_design_controller**: Generate parameters by default.

### Keycap

Defines the keycap function and the model generation mechanism.

- **keycap_function**: Represents the behavior of a single keycap, determining its effect based on given parameters.
- **generate_keycaps**: Produces a list of multiple keycap functions.
- **generate_model**: Creates the model as a linear combination of `n` keycap functions.

### Controller

The `Controller` class manages parameters and constraints for the keycap model. It ensures the keyboard model operates correctly by constraining the generated values.

- **generate_n**: Randomly generates `n` values.
- **generate_D**: Randomly produces `D` values.
- **generate_alpha**: Produces alpha values.
- **generate_w**: Generates w values based on an increasing pattern.
- **generate_model_values**: Creates model values for a given time series and enforces velocity constraints.

### ConfigurationManager

The `ConfigurationManager` class is essential for maintaining session consistency. It offers methods to save and retrieve configurations for controllers. This ensures that a session can continue with the same characteristics, offering a seamless user experience.

- **save**: Saves a controller's configuration.
- **load**: Retrieves a saved controller configuration.

### How to use

This demonstration will show you how to generate model values and convert velocities to time durations.

#### The code

```python
from keycap import Controller, ConfigurationManager, Plant

if __name__ == "__main__":
    # Initialization:

    # Create an instance of the Controller class.
    controller = Controller()

    # Create an instance of the ConfigurationManager for saving/loading configurations.
    manager = ConfigurationManager()

    # Instantiate a Plant with the above controller.
    plant = Plant(controller)

    # Default design the controller
    plant.default_design_controller()

    # Generate model values:
    t = np.linspace(0, 1, 1000)
    velocities = plant.generate_model(t)

    # Convert the generated velocities to time durations between key presses.
    times = plant.velocities_to_time(velocities)

    # Print the results:
    print("Velocities: ", velocities)
    print("Times: ", times)
```

#### Explanation:
##### Initialization:

Controller Instance: We start by creating an instance of the Controller class. This will be our main controller to manage parameters for the keyboard model.
ConfigurationManager Instance: This is used to save and load the configurations of our controllers. It's essential if you want the model's behavior to remain consistent across sessions.
Plant Creation:

The Plant object is essentially the system being controlled by the Controller. In this context, the Plant simulates the behavior of the keyboard.
##### Custom Design (Optional):

It is possible to set values for the controller's parameters. Read the Controller documentation for more information. You can redfine custom logic for the parameters D,w which determines the velocity of the keycap.

##### Generating Model Values:

Using ```np.linspace(0, 1, 1000)```, we're creating a linear space of 1000 time points between 0 and 1.
plant.generate_model(t) will use the current controller configuration to generate velocities over this time range.

##### Output:

With plant.velocities_to_time(velocities), we convert the velocities to difference in key press times. 
You can call plant.generate_model(t) multiple times to generate different variations of the model.
Then you can take the timing differences and assign them to the key presses of a keyboard.

#####  Configuration Management:
One of the powerful features is the ability to save and load configurations using the ConfigurationManager. The manager object can be used to save your controller's configuration and later load it. This ensures consistency in the model's behavior across different sessions.

# Example usage to save and load configuration:
```python
controller.save_configuration(manager, "UID")
loaded_controller = Controller.load_configuration(manager, "UID")
```

This is important for bypassing detection system!
