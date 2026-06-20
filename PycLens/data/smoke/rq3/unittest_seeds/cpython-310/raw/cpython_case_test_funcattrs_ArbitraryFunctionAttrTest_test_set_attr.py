# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: ArbitraryFunctionAttrTest_test_set_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.b.known_attr = 7
    self.assertEqual(self.b.known_attr, 7)
    try:
        self.fi.a.known_attr = 7
    except AttributeError:
        pass
    else:
        self.fail('setting attributes on methods should raise error')
