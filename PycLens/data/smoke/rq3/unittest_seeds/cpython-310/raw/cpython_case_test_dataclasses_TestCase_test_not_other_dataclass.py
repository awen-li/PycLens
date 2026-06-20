# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_not_other_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Point3D:
        x: int
        y: int
        z: int

    @dataclass
    class Date:
        year: int
        month: int
        day: int
    self.assertNotEqual(Point3D(2017, 6, 3), Date(2017, 6, 3))
    self.assertNotEqual(Point3D(1, 2, 3), (1, 2, 3))
    with self.assertRaisesRegex(TypeError, 'unpack'):
        (x, y, z) = Point3D(4, 5, 6)

    @dataclass
    class Point3Dv1:
        x: int = 0
        y: int = 0
        z: int = 0
    self.assertNotEqual(Point3D(0, 0, 0), Point3Dv1())
