# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shelve.py
# case: TestCase_test_open_template

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(self.dirname)
    self.addCleanup(os_helper.rmtree, self.dirname)
    s = shelve.open(self.fn, protocol=protocol)
    try:
        s['key1'] = (1, 2, 3, 4)
        self.assertEqual(s['key1'], (1, 2, 3, 4))
    finally:
        s.close()
