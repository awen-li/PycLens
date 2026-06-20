# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shelve.py
# case: TestCase_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = {}
    s = shelve.Shelf(d1, protocol=2, writeback=False)
    s['key1'] = [1, 2, 3, 4]
    self.assertEqual(s['key1'], [1, 2, 3, 4])
    self.assertEqual(len(s), 1)
    s.close()
    self.assertRaises(ValueError, len, s)
    try:
        s['key1']
    except ValueError:
        pass
    else:
        self.fail('Closed shelf should not find a key')
