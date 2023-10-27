import unittest
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..plant import Plant
import pyautogui
import time

class TestPlantOutput(unittest.TestCase):

    def setUp(self):
        # This method will be called before every test
        self.plant = Plant()
        self.text = "hello guys here we are testing the performance of the keycap equation when writing text"
        self.t = np.linspace(0, 1, 1000)

    def test_velocity_to_keypress(self):
        self.plant.default_design_controller()

        # Generate model values (velocities)
        velocities = self.plant.generate_model(self.t)

        # Ensure the text isn't longer than the velocities array
        if len(self.text) > len(velocities):
            raise ValueError("Text ishello guys here we are testing ththe keycAuation w longer than available velocities!")
        
        for i, vel in enumerate(velocities):
            # Calculate the time difference from the velocity
            time_diff = 1 / (vel)
            print("Waiting time: ", time_diff, vel)

            # Wait for the calculated time difference
            time.sleep(time_diff)

            if (i >= len(self.text)):
                break

            # Simulate keypress using pyautogui
            letter = self.text[i]
            pyautogui.press(letter)

        print ("Finished typing text!")


if __name__ == "__main__":
    unittest.main()

