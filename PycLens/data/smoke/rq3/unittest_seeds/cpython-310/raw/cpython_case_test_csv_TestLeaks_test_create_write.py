# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestLeaks_test_create_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    delta = 0
    lastrc = sys.gettotalrefcount()
    s = NUL()
    for i in range(20):
        gc.collect()
        self.assertEqual(gc.garbage, [])
        rc = sys.gettotalrefcount()
        csv.writer(s)
        csv.writer(s)
        csv.writer(s)
        delta = rc - lastrc
        lastrc = rc
    self.assertLess(delta, 3)
