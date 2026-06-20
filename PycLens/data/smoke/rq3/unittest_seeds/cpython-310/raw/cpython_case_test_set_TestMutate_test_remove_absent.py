# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestMutate_test_remove_absent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        self.set.remove('d')
        self.fail('Removing missing element should have raised LookupError')
    except LookupError:
        pass
