# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shelve.py
# case: TestCase_test_writeback_also_writes_immediately

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    key = 'key'
    encodedkey = key.encode('utf-8')
    with shelve.Shelf(d, writeback=True) as s:
        s[key] = [1]
        p1 = d[encodedkey]
        s['key'].append(2)
    p2 = d[encodedkey]
    self.assertNotEqual(p1, p2)
