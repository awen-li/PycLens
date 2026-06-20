# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceExceptions_test_bases_raises_other_than_attribute_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class E(object):

        def getbases(self):
            raise RuntimeError
        __bases__ = property(getbases)

    class I(object):

        def getclass(self):
            return E()
        __class__ = property(getclass)

    class C(object):

        def getbases(self):
            return ()
        __bases__ = property(getbases)
    self.assertRaises(RuntimeError, isinstance, I(), C())
