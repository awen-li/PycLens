# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FilterTestCase_test_sep

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    normsep = os.path.normcase('\\') == os.path.normcase('/')
    self.assertEqual(filter(['usr/bin', 'usr', 'usr\\lib'], 'usr/*'), ['usr/bin', 'usr\\lib'] if normsep else ['usr/bin'])
    self.assertEqual(filter(['usr/bin', 'usr', 'usr\\lib'], 'usr\\*'), ['usr/bin', 'usr\\lib'] if normsep else ['usr\\lib'])
