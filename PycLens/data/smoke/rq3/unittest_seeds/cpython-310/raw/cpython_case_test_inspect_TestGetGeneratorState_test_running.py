# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetGeneratorState_test_running

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def running_check_generator():
        for number in range(5):
            self.assertEqual(self._generatorstate(), inspect.GEN_RUNNING)
            yield number
            self.assertEqual(self._generatorstate(), inspect.GEN_RUNNING)
    self.generator = running_check_generator()
    next(self.generator)
    next(self.generator)
