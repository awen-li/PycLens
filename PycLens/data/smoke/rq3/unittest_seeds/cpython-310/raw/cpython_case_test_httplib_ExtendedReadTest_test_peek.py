# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: ExtendedReadTest_test_peek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    resp = self.resp
    oldpeek = resp.fp.peek

    def mypeek(n=-1):
        p = oldpeek(n)
        if n >= 0:
            return p[:n]
        return p[:10]
    resp.fp.peek = mypeek
    all = []
    while True:
        p = resp.peek(3)
        if p:
            self.assertGreater(len(p), 0)
            p2 = resp.peek()
            self.assertGreaterEqual(len(p2), len(p))
            self.assertTrue(p2.startswith(p))
            next = resp.read(len(p2))
            self.assertEqual(next, p2)
        else:
            next = resp.read()
            self.assertFalse(next)
        all.append(next)
        if not next:
            break
    self.assertEqual(b''.join(all), self.lines_expected)
