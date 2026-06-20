# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestExceptionPropagation_test_changingSizeWhileIterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = set([1, 2, 3])
    try:
        for i in s:
            s.update([4])
    except RuntimeError:
        pass
    else:
        self.fail('no exception when changing size during iteration')
