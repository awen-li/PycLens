# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_dis_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        del sys.last_traceback
    except AttributeError:
        pass
    self.assertRaises(RuntimeError, dis.dis, None)
