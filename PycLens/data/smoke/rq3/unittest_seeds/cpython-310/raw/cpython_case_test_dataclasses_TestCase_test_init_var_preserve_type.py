# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_init_var_preserve_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(InitVar[int].type, int)
    self.assertEqual(repr(InitVar[int]), 'dataclasses.InitVar[int]')
    self.assertEqual(repr(InitVar[List[int]]), 'dataclasses.InitVar[typing.List[int]]')
    self.assertEqual(repr(InitVar[list[int]]), 'dataclasses.InitVar[list[int]]')
    self.assertEqual(repr(InitVar[int | str]), 'dataclasses.InitVar[int | str]')
