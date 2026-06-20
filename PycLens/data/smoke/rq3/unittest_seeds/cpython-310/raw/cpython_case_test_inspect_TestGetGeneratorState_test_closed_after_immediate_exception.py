# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetGeneratorState_test_closed_after_immediate_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(RuntimeError):
        self.generator.throw(RuntimeError)
    self.assertEqual(self._generatorstate(), inspect.GEN_CLOSED)
