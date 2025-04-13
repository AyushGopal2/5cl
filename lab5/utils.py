import numpy as np

'''This converts a given wavelength of light to an 
approximate RGB color value. The wavelength must be given
in nanometers in the range from 380 nm through 750 nm
(789 THz through 400 THz).

Original code by Dan Bruton
http://www.physics.sfasu.edu/astro/color/spectra.html

Python code by https://gist.github.com/error454/65d7f392e1acd4a782fc
Modified for Numpy by ChatGPT
'''

def wavelength_to_rgb(wavelengths, gamma=0.8):
    wavelengths = np.asarray(wavelengths, dtype=float)
    R = np.zeros_like(wavelengths)
    G = np.zeros_like(wavelengths)
    B = np.zeros_like(wavelengths)
    
    # Define conditions
    cond1 = (wavelengths >= 380) & (wavelengths <= 440)
    cond2 = (wavelengths > 440) & (wavelengths <= 490)
    cond3 = (wavelengths > 490) & (wavelengths <= 510)
    cond4 = (wavelengths > 510) & (wavelengths <= 580)
    cond5 = (wavelengths > 580) & (wavelengths <= 645)
    cond6 = (wavelengths > 645) & (wavelengths <= 750)
    
    # Apply calculations based on conditions
    attenuation = 0.3 + 0.7 * (wavelengths - 380) / (440 - 380)
    R[cond1] = ((-(wavelengths[cond1] - 440) / (440 - 380)) * attenuation[cond1]) ** gamma
    B[cond1] = (1.0 * attenuation[cond1]) ** gamma
    
    G[cond2] = ((wavelengths[cond2] - 440) / (490 - 440)) ** gamma
    B[cond2] = 1.0
    
    G[cond3] = 1.0
    B[cond3] = (-(wavelengths[cond3] - 510) / (510 - 490)) ** gamma
    
    R[cond4] = ((wavelengths[cond4] - 510) / (580 - 510)) ** gamma
    G[cond4] = 1.0
    
    R[cond5] = 1.0
    G[cond5] = (-(wavelengths[cond5] - 645) / (645 - 580)) ** gamma
    
    attenuation = 0.3 + 0.7 * (750 - wavelengths) / (750 - 645)
    R[cond6] = (1.0 * attenuation[cond6]) ** gamma

    
    # Stack into an array of RGB tuples
    return np.stack([R, G, B], axis=-1)