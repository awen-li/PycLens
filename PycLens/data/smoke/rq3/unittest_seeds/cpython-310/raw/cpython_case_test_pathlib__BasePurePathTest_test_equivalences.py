# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_equivalences

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (k, tuples) in self.equivalences.items():
        canon = k.replace('/', self.sep)
        posix = k.replace(self.sep, '/')
        if canon != posix:
            tuples = tuples + [tuple((part.replace('/', self.sep) for part in t)) for t in tuples]
            tuples.append((posix,))
        pcanon = self.cls(canon)
        for t in tuples:
            p = self.cls(*t)
            self.assertEqual(p, pcanon, 'failed with args {}'.format(t))
            self.assertEqual(hash(p), hash(pcanon))
            self.assertEqual(str(p), canon)
            self.assertEqual(p.as_posix(), posix)
