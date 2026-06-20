# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: ArbitraryFunctionAttrTest_test_unset_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for func in [self.b, self.fi.a]:
        try:
            func.non_existent_attr
        except AttributeError:
            pass
        else:
            self.fail('using unknown attributes should raise AttributeError')
