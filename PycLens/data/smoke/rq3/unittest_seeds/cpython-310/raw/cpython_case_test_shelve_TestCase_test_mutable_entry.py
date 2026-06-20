# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shelve.py
# case: TestCase_test_mutable_entry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = byteskeydict()
    with shelve.Shelf(d1, protocol=2, writeback=False) as s:
        s['key1'] = [1, 2, 3, 4]
        self.assertEqual(s['key1'], [1, 2, 3, 4])
        s['key1'].append(5)
        self.assertEqual(s['key1'], [1, 2, 3, 4])
    d2 = byteskeydict()
    with shelve.Shelf(d2, protocol=2, writeback=True) as s:
        s['key1'] = [1, 2, 3, 4]
        self.assertEqual(s['key1'], [1, 2, 3, 4])
        s['key1'].append(5)
        self.assertEqual(s['key1'], [1, 2, 3, 4, 5])
    self.assertEqual(len(d1), 1)
    self.assertEqual(len(d2), 1)
