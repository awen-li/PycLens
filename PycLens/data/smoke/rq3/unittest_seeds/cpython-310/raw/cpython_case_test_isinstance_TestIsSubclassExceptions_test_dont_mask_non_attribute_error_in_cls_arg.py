# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsSubclassExceptions_test_dont_mask_non_attribute_error_in_cls_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B:
        pass

    class C(object):

        def getbases(self):
            raise RuntimeError
        __bases__ = property(getbases)
    self.assertRaises(RuntimeError, issubclass, B, C())
