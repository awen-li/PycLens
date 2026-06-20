# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = make_dataclass('C', [('x', int), ('y', int, field(default=5))], namespace={'add_one': lambda self: self.x + 1})
    c = C(10)
    self.assertEqual((c.x, c.y), (10, 5))
    self.assertEqual(c.add_one(), 11)
