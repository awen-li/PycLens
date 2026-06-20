# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_default_case_sensitivity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig({'foo': 'Bar'})
    self.assertEqual(cf.get(self.default_section, 'Foo'), 'Bar', 'could not locate option, expecting case-insensitive option names')
    cf = self.newconfig({'Foo': 'Bar'})
    self.assertEqual(cf.get(self.default_section, 'Foo'), 'Bar', 'could not locate option, expecting case-insensitive defaults')
