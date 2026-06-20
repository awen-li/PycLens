# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_multiple_dumps_and_loads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = (1, 'abc', b'def', 1.0, (2, 'a', ['b', b'c']))
    for interleaved in (b'', b'0123'):
        ilen = len(interleaved)
        positions = []
        try:
            with open(os_helper.TESTFN, 'wb') as f:
                for d in data:
                    marshal.dump(d, f)
                    if ilen:
                        f.write(interleaved)
                    positions.append(f.tell())
            with open(os_helper.TESTFN, 'rb') as f:
                for (i, d) in enumerate(data):
                    self.assertEqual(d, marshal.load(f))
                    if ilen:
                        f.read(ilen)
                    self.assertEqual(positions[i], f.tell())
        finally:
            os_helper.unlink(os_helper.TESTFN)
