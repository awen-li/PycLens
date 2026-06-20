# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestTraceback_test_sets_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise IndexError()
    except IndexError as e:
        self.assertIsInstance(e.__traceback__, types.TracebackType)
    else:
        self.fail('No exception raised')
