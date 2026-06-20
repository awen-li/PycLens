# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMakeDataclass_test_other_params

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = make_dataclass('C', [('x', int), ('y', ClassVar[int], 10), ('z', ClassVar[int], field(default=20))], init=False)
    self.assertNotIn('__init__', vars(C))
    self.assertIn('__repr__', vars(C))
    with self.assertRaisesRegex(TypeError, 'unexpected keyword argument'):
        C = make_dataclass('C', [], xxinit=False)
