import unittest
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller import Controller
from controller import ConfigurationManager


class TestControllerConfiguration(unittest.TestCase):

    def setUp(self):
        self.n = 500
        self.D = np.random.uniform(0.1, 5, self.n)
        self.alpha = np.full(self.n, 1)
        self.controller = Controller(n=self.n, D=self.D)
        self.manager = ConfigurationManager()

    def test_save_and_load_configuration(self):
        # Save the configuration
        config_name = "UID"
        self.controller.save_configuration(self.manager, config_name)

        # Load the configuration
        loaded_controller = Controller.load_configuration(self.manager, config_name)

        # Verify the loaded configuration matches the original
        np.testing.assert_array_almost_equal(self.controller.D, loaded_controller.D)
        np.testing.assert_array_almost_equal(self.controller.alpha, loaded_controller.alpha)
        np.testing.assert_array_almost_equal(self.controller.w, loaded_controller.w)
        self.assertEqual(self.controller.min_velocity, loaded_controller.min_velocity)
        self.assertEqual(self.controller.max_velocity, loaded_controller.max_velocity)

    def plot_comparison(self, original_controller, loaded_controller):
        """
        Plots a comparison between the original and loaded configurations for D, alpha, w, and model values.
        """
        t = np.linspace(0, 1, 1000)  # example time series
        original_model_values = original_controller.generate_model_values(t)
        loaded_model_values = loaded_controller.generate_model_values(t)

        fig, axs = plt.subplots(4, 1, figsize=(10, 10))

        # Plot D values
        axs[0].plot(original_controller.D, label='Original D', color='blue')
        axs[0].plot(loaded_controller.D, label='Loaded D', color='red', linestyle='--')
        axs[0].set_title("D values")
        axs[0].legend()

        # Plot alpha values
        axs[1].plot(original_controller.alpha, label='Original alpha', color='blue')
        axs[1].plot(loaded_controller.alpha, label='Loaded alpha', color='red', linestyle='--')
        axs[1].set_title("alpha values")
        axs[1].legend()

        # Plot w values
        axs[2].plot(original_controller.w, label='Original w', color='blue')
        axs[2].plot(loaded_controller.w, label='Loaded w', color='red', linestyle='--')
        axs[2].set_title("w values")
        axs[2].legend()

        # Plot model values
        axs[3].plot(t, original_model_values, label='Original Model', color='blue')
        axs[3].plot(t, loaded_model_values, label='Loaded Model', color='red', linestyle='--')
        axs[3].set_title("Model values over time")
        axs[3].legend()

        plt.tight_layout()
        plt.show()

    def test_error_on_missing_configuration(self):

        # Save the configuration
        config_name = "UID"
        self.controller.save_configuration(self.manager, config_name)

        # Load the configuration
        loaded_controller = Controller.load_configuration(self.manager, config_name)

        # Attempting to load a non-existent configuration should raise an error
        with self.assertRaises(ValueError):
            Controller.load_configuration(self.manager, "non_existent_config")

        self.plot_comparison(self.controller, loaded_controller)



if __name__ == "__main__":
    unittest.main()
