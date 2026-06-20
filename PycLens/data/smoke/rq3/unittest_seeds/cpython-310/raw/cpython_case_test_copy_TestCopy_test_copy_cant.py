# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_cant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __getattribute__(self, name):
            if name.startswith('__reduce'):
                raise AttributeError(name)
            return object.__getattribute__(self, name)
    x = C()
    self.assertRaises(copy.Error, copy.copy, x)
