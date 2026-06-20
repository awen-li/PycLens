# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = []
    undocumented = {'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'Quoter', 'ResultBase', 'clear_cache', 'to_bytes', 'unwrap'}
    for name in dir(urllib.parse):
        if name.startswith('_') or name in undocumented:
            continue
        object = getattr(urllib.parse, name)
        if getattr(object, '__module__', None) == 'urllib.parse':
            expected.append(name)
    self.assertCountEqual(urllib.parse.__all__, expected)
