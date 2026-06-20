# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: AAAPTypesLongInitTest_test_pytype_long_ready

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UserLong(object):

        def __pow__(self, *args):
            pass
    try:
        pow(0, UserLong(), 0)
    except:
        pass
    type.mro(tuple)
