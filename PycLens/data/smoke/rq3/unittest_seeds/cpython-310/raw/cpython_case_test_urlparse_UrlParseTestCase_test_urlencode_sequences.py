# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_urlencode_sequences

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = urllib.parse.urlencode({'a': [1, 2], 'b': (3, 4, 5)}, True)
    assert set(result.split('&')) == {'a=1', 'a=2', 'b=3', 'b=4', 'b=5'}

    class Trivial:

        def __str__(self):
            return 'trivial'
    result = urllib.parse.urlencode({'a': Trivial()}, True)
    self.assertEqual(result, 'a=trivial')
