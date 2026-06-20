# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_no_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = make_dataclass('Point', ['x', 'y', 'z'])
    c = C(1, 2, 3)
    self.assertEqual(vars(c), {'x': 1, 'y': 2, 'z': 3})
    self.assertEqual(C.__annotations__, {'x': 'typing.Any', 'y': 'typing.Any', 'z': 'typing.Any'})
    C = make_dataclass('Point', ['x', ('y', int), 'z'])
    c = C(1, 2, 3)
    self.assertEqual(vars(c), {'x': 1, 'y': 2, 'z': 3})
    self.assertEqual(C.__annotations__, {'x': 'typing.Any', 'y': int, 'z': 'typing.Any'})
