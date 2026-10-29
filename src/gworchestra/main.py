import matplotlib.pyplot as plt
import numpy as np
from bilby.gw.waveform_generator import WaveformGenerator
from bilby.gw.source import lal_binary_black_hole

# Constants
speed_of_light = 299792458.0  # m/s
parsec = 3.085677581491367e16  # m
solar_mass = 1.988409870698050731911960804878414216e30  # Kg
mtsun = 4.925490947641266978197229498498379006e-6
radius_of_earth = 6378136.6  # m
gravitational_constant = 6.6743e-11  # m^3 kg^-1 s^-2

# Black hole parameters
mass_1 = 0
mass_2 = 0
f0 = 20

# Coalescense constants
t0 = 0  # = time of merger
phi_c = 0  # = gravitational wave phase at merger


def zero_pn_time_to_merger(frequency, mass_1, mass_2):
    mtot = mass_1 + mass_2
    eta = mass_1 * mass_2 / (mtot * mtot)
    v = np.cbrt(np.pi * mtot * mtsun * frequency)
    return (5 * mtot * mtsun) / (256 * v**8 * eta)


def main() -> None:
    print("Hello from black-hole-fun!")

    # implementation
    mass_1 = 1.4
    mass_2 = 1.4
    time_of_merger = zero_pn_time_to_merger(f0, mass_1, mass_2)
    print(f"time of merger: { time_of_merger }")

    src_params = dict(
        mass_1              = mass_1,
        mass_2              = mass_2,
        luminosity_distance = 100,
        a_1                 = 0,
        tilt_1              = 0,
        phi_12              = 0,
        a_2                 = 0,
        tilt_2              = 0,
        phi_jl              = 0,
        theta_jn            = 0,
        phase               = 0,
    )

    wfg = WaveformGenerator(
        4096,
        time_of_merger,
        frequency_domain_source_model=lal_binary_black_hole,
        waveform_arguments={
            'source_model' : 'TaylorF2',
            'minimum_frequency' : 
        }
        )



main()
