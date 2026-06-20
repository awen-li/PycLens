# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Planet(Enum):
        MERCURY = (3.303e+23, 2439700.0)
        VENUS = (4.869e+24, 6051800.0)
        EARTH = (5.976e+24, 6378140.0)
        MARS = (6.421e+23, 3397200.0)
        JUPITER = (1.9e+27, 71492000.0)
        SATURN = (5.688e+26, 60268000.0)
        URANUS = (8.686e+25, 25559000.0)
        NEPTUNE = (1.024e+26, 24746000.0)

        def __init__(self, mass, radius):
            self.mass = mass
            self.radius = radius

        @property
        def surface_gravity(self):
            G = 6.673e-11
            return G * self.mass / (self.radius * self.radius)
    self.assertEqual(round(Planet.EARTH.surface_gravity, 2), 9.8)
    self.assertEqual(Planet.EARTH.value, (5.976e+24, 6378140.0))
