# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:

        class C(bool):
            pass
    except TypeError:
        pass
    else:
        self.fail('bool should not be subclassable')
    self.assertRaises(TypeError, int.__new__, bool, 0)
