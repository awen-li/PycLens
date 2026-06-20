# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_random

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import random
    d = {}
    for dummy in range(5):
        with contextlib.closing(dumbdbm.open(_fname)) as f:
            for dummy in range(100):
                k = random.choice('abcdefghijklm')
                if random.random() < 0.2:
                    if k in d:
                        del d[k]
                        del f[k]
                else:
                    v = random.choice((b'a', b'b', b'c')) * random.randrange(10000)
                    d[k] = v
                    f[k] = v
                    self.assertEqual(f[k], v)
        with contextlib.closing(dumbdbm.open(_fname)) as f:
            expected = sorted(((k.encode('latin-1'), v) for (k, v) in d.items()))
            got = sorted(f.items())
            self.assertEqual(expected, got)
