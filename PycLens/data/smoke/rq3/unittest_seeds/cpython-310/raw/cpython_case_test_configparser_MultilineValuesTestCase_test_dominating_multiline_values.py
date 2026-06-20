# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: MultilineValuesTestCase_test_dominating_multiline_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf_from_file = self.newconfig()
    with open(os_helper.TESTFN, encoding='utf-8') as f:
        cf_from_file.read_file(f)
    self.assertEqual(cf_from_file.get('section8', 'lovely_spam4'), self.wonderful_spam.replace('\t\n', '\n'))
