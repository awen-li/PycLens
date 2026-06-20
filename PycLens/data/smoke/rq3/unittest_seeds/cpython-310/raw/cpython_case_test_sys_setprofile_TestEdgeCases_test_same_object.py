# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_setprofile.py
# case: TestEdgeCases_test_same_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(*args):
        ...
    sys.setprofile(foo)
    del foo
    sys.setprofile(sys.getprofile())
