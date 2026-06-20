# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestCause_test_erroneous_cause

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyException(Exception):

        def __init__(self):
            raise RuntimeError()
    try:
        raise IndexError from MyException
    except RuntimeError:
        pass
    else:
        self.fail('No exception raised')
