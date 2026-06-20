# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: SignalAndYieldFromTest_test_raise_and_yield_from

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gen = self.generator1()
    gen.send(None)
    try:
        _testcapi.raise_SIGINT_then_send_None(gen)
    except BaseException as _exc:
        exc = _exc
    self.assertIs(type(exc), StopIteration)
    self.assertEqual(exc.value, 'PASSED')
