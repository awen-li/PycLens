# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestLeaks_test_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    delta = 0
    rows = ['a,b,c\r\n'] * 5
    lastrc = sys.gettotalrefcount()
    for i in range(20):
        gc.collect()
        self.assertEqual(gc.garbage, [])
        rc = sys.gettotalrefcount()
        rdr = csv.reader(rows)
        for row in rdr:
            pass
        delta = rc - lastrc
        lastrc = rc
    self.assertLess(delta, 5)
