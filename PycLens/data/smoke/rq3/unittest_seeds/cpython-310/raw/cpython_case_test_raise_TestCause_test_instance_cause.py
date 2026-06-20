# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestCause_test_instance_cause

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cause = KeyError()
    try:
        raise IndexError from cause
    except IndexError as e:
        self.assertIs(e.__cause__, cause)
    else:
        self.fail('No exception raised')
