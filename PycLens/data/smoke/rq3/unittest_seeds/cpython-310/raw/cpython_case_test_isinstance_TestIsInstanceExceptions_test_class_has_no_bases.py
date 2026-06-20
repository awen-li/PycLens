# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceExceptions_test_class_has_no_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class I(object):

        def getclass(self):
            return None
        __class__ = property(getclass)

    class C(object):

        def getbases(self):
            return ()
        __bases__ = property(getbases)
    self.assertEqual(False, isinstance(I(), C()))
