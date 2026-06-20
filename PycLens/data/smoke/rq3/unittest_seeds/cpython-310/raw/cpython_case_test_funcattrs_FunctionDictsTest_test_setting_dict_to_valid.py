# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionDictsTest_test_setting_dict_to_valid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'known_attr': 7}
    self.b.__dict__ = d
    self.assertIs(d, self.b.__dict__)
    self.F.a.__dict__ = d
    self.assertIs(d, self.fi.a.__func__.__dict__)
    self.assertIs(d, self.fi.a.__dict__)
    self.assertEqual(self.b.known_attr, 7)
    self.assertEqual(self.b.__dict__['known_attr'], 7)
    self.assertEqual(self.fi.a.__func__.known_attr, 7)
    self.assertEqual(self.fi.a.known_attr, 7)
