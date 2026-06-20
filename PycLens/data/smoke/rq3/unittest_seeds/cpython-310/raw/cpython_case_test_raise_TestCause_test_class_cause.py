# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestCause_test_class_cause

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise IndexError from KeyError
    except IndexError as e:
        self.assertIsInstance(e.__cause__, KeyError)
    else:
        self.fail('No exception raised')
