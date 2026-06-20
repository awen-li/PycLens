# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRemovedFunctionality_test_tuples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise (IndexError, KeyError)
    except TypeError:
        pass
    else:
        self.fail('No exception raised')
