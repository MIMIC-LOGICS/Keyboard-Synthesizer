import numpy as np

# Define the keycap function, which is used to generate keyboard time series data
# D: the amplitude of the keycap, the greater the value, the faster the keyboard writes. In the frequency domain the greater the value, the higher the amplitude of the gaussian function
# alpha: the damping coefficient of the keycap, variation in the velocity. In the frequency domain the greater the value, the narrower the gaussian function (propotional to the standard deviation)
# t: time variable
# w: the frequency of the keycap, it represents the number of gaussian functions in the frequency domain. Each gaussian function is shifted by w, and the greater the value, the more gaussian functions there are, and the more complex the keyboard writing is
keycap_function = lambda D, alpha, t, w: D / alpha * (np.exp (-(t)**2/(4 * alpha)) * np.cos(w*t))

# Generate the model keeping t as a variable and D, alpha, w as parameters of the function
# The model is a linear combination of n keycaps
def generate_keycaps(n, D, alpha, w):
    """
    Generate a list of n keycap functions.
    
    Parameters:
    - n (int): Number of keycap functions to generate.
    - D (list of floats): List of amplitude factors. Length should be n.
    - alpha (list of floats): List of parameters affecting the shape of the keycap. Length should be n.
    - w (list of floats): List of frequencies. Length should be n.
    
    Returns:
    - (list of functions): List of keycap functions.
    """
    if not all(len(lst) == n for lst in [D, alpha, w]):
        raise ValueError("Lengths of D, alpha, and w should be equal to n.")
    
    keycaps = []
    for i in range(n):
        keycap = lambda t, D=D[i], alpha=alpha[i], w=w[i]: keycap_function(D, alpha, t, w)
        keycaps.append(keycap)
    
    return keycaps

def generate_model(t, n, D, alpha, w):
    """
    Generate the model as a linear combination of n keycap functions.
    
    Parameters:
    - t (array-like): Time series data.
    - n (int): Number of keycap functions to generate.
    - D (list of floats): List of amplitude factors. Length should be n.
    - alpha (list of floats): List of parameters affecting the shape of the keycap. Length should be n.
    - w (list of floats): List of frequencies. Length should be n.
    
    Returns:
    - (array-like): Values of the model for the given time series.
    """
    keycaps = generate_keycaps(n, D, alpha, w)
    model = sum(keycap(t) for keycap in keycaps)

    # Ensure all values are non-negative
    model = np.abs(model)

    return model