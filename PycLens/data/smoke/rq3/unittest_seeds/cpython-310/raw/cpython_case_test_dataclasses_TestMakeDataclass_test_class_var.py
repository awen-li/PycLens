# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_class_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = make_dataclass('C', [('x', int), ('y', ClassVar[int], 10), ('z', ClassVar[int], field(default=20))])
    c = C(1)
    self.assertEqual(vars(c), {'x': 1})
    self.assertEqual(len(fields(c)), 1)
    self.assertEqual(C.y, 10)
    self.assertEqual(C.z, 20)
