# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestLeaks_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    delta = 0
    rows = [[1, 2, 3]] * 5
    s = NUL()
    lastrc = sys.gettotalrefcount()
    for i in range(20):
        gc.collect()
        self.assertEqual(gc.garbage, [])
        rc = sys.gettotalrefcount()
        writer = csv.writer(s)
        for row in rows:
            writer.writerow(row)
        delta = rc - lastrc
        lastrc = rc
    self.assertLess(delta, 5)
