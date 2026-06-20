# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: BaseLocalTest_test_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyLocal(self._local):

        def __init__(self, *args, **kwargs):
            pass
    MyLocal(a=1)
    MyLocal(1)
    self.assertRaises(TypeError, self._local, a=1)
    self.assertRaises(TypeError, self._local, 1)
