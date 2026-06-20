# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceExceptions_test_mask_attribute_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class I:
        pass

    class C(object):

        def getbases(self):
            raise AttributeError
        __bases__ = property(getbases)
    self.assertRaises(TypeError, isinstance, I(), C())
