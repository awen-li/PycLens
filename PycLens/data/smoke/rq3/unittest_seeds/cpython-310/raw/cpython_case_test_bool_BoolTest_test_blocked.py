# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_blocked

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        __bool__ = None
    self.assertRaises(TypeError, bool, A())

    class B:

        def __len__(self):
            return 10
        __bool__ = None
    self.assertRaises(TypeError, bool, B())
