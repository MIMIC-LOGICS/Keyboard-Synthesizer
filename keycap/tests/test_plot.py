import sys
import os
import unittest
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller import Controller

class TestPlot(unittest.TestCase):

    def setUp(self):
        """Setup method called before every test."""
        self.controller = Controller(n=600)
        
    def test_plot_time_series(self):
        """Test to visually inspect the generated time series."""
        t = np.linspace(0, 1, 1000)
        self.controller.generate_D()
        self.controller.generate_alpha()
        self.controller.generate_w()
        model_values = self.controller.generate_model_values(t)
        plt.plot(t, model_values, label="Controller 1")

        controller2 = Controller(n=600)
        controller2.generate_D()
        controller2.generate_alpha()
        controller2.generate_w()
        model_values2 = controller2.generate_model_values(t)
        plt.plot(t, model_values2, label="Controller 2")

        plt.title("Comparison of Different Time Series")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid(True)
        plt.legend()
        plt.show()



if __name__ == "__main__":
    unittest.main()