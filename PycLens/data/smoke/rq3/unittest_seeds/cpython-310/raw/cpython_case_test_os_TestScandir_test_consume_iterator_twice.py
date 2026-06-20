# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_consume_iterator_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.create_file('file.txt')
    iterator = os.scandir(self.path)
    entries = list(iterator)
    self.assertEqual(len(entries), 1, entries)
    entries2 = list(iterator)
    self.assertEqual(len(entries2), 0, entries2)
