# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetGeneratorState_test_getgeneratorlocals_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def yield_one():
        yield 1
    one = yield_one()
    self.assertEqual(inspect.getgeneratorlocals(one), {})
    try:
        next(one)
    except StopIteration:
        pass
    self.assertEqual(inspect.getgeneratorlocals(one), {})
