# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: InstancemethodAttrTest_test___func___non_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fi.id = types.MethodType(id, self.fi)
    self.assertEqual(self.fi.id(), id(self.fi))
    try:
        self.fi.id.unknown_attr
    except AttributeError:
        pass
    else:
        self.fail('using unknown attributes should raise AttributeError')
    self.cannot_set_attr(self.fi.id, 'unknown_attr', 2, AttributeError)
