# Source Generated with Decompyle++
# File: cpython-312-adab23e05ec4.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class Planet(Enum):
        MERCURY = (3.303e+23, 2.4397e+06)
        VENUS = (4.869e+24, 6.0518e+06)
        EARTH = (5.976e+24, 6.37814e+06)
        MARS = (6.421e+23, 3.3972e+06)
        JUPITER = (1.9e+27, 7.1492e+07)
        SATURN = (5.688e+26, 6.0268e+07)
        URANUS = (8.686e+25, 2.5559e+07)
        NEPTUNE = (1.024e+26, 2.4746e+07)
        
        def __init__(self, mass, radius):
            self.mass = mass
            self.radius = radius

        surface_gravity = (lambda self: G = 6.673e-11G * self.mass / (self.radius * self.radius))()

    self.assertEqual(round(Planet.EARTH.surface_gravity, 2), 9.8)
    self.assertEqual(Planet.EARTH.value, (5.976e+24, 6.37814e+06))

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
