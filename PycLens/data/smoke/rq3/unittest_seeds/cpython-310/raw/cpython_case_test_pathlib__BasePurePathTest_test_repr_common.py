# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_repr_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for pathstr in ('a', 'a/b', 'a/b/c', '/', '/a/b', '/a/b/c'):
        p = self.cls(pathstr)
        clsname = p.__class__.__name__
        r = repr(p)
        self.assertTrue(r.startswith(clsname + '('), r)
        self.assertTrue(r.endswith(')'), r)
        inner = r[len(clsname) + 1:-1]
        self.assertEqual(eval(inner), p.as_posix())
        q = eval(r, pathlib.__dict__)
        self.assertIs(q.__class__, p.__class__)
        self.assertEqual(q, p)
        self.assertEqual(repr(q), r)
