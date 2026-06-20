# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: ArbitraryFunctionAttrTest_test_delete_unknown_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        del self.b.unknown_attr
    except AttributeError:
        pass
    else:
        self.fail('deleting unknown attribute should raise TypeError')
