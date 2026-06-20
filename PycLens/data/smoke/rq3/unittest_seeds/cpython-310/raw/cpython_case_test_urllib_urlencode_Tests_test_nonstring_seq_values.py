# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlencode_Tests_test_nonstring_seq_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('a=1&a=2', urllib.parse.urlencode({'a': [1, 2]}, True))
    self.assertEqual('a=None&a=a', urllib.parse.urlencode({'a': [None, 'a']}, True))
    data = collections.OrderedDict([('a', 1), ('b', 1)])
    self.assertEqual('a=a&a=b', urllib.parse.urlencode({'a': data}, True))
