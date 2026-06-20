# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_keyword_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pat = re.compile('(ab)')
    self.assertEqual(pat.match(string='abracadabra', pos=7, endpos=10).span(), (7, 9))
    self.assertEqual(pat.fullmatch(string='abracadabra', pos=7, endpos=9).span(), (7, 9))
    self.assertEqual(pat.search(string='abracadabra', pos=3, endpos=10).span(), (7, 9))
    self.assertEqual(pat.findall(string='abracadabra', pos=3, endpos=10), ['ab'])
    self.assertEqual(pat.split(string='abracadabra', maxsplit=1), ['', 'ab', 'racadabra'])
    self.assertEqual(pat.scanner(string='abracadabra', pos=3, endpos=10).search().span(), (7, 9))
