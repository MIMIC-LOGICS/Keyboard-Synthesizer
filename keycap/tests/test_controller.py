import sys
import os
import unittest
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        """Setup method called before every test."""
        self.controller = Controller(n=5)

    def test_generate_D(self):
        """Test generate_D method."""
        self.controller.generate_D()
        self.assertEqual(len(self.controller.D), 5)
        self.assertTrue(all(0.1 <= d <= 6 for d in self.controller.D))

    def test_generate_alpha(self):
        """Test generate_alpha method."""
        self.controller.generate_alpha()
        self.assertEqual(len(self.controller.alpha), 5)
        self.assertTrue(all(a == 1 for a in self.controller.alpha))

    def test_generate_w(self):
        """Test generate_w method."""
        self.controller.generate_w()
        self.assertEqual(len(self.controller.w), 5)

    def test_generate_model_values(self):
        """Test generate_model_values method."""
        t = np.linspace(0, 1, 1000)
        
        # Now set the parameters and check the output
        self.controller.generate_D()
        self.controller.generate_alpha()
        self.controller.generate_w()

        model_values = self.controller.generate_model_values(t)
        self.assertEqual(len(model_values), len(t))


if __name__ == "__main__":
    unittest.main()
