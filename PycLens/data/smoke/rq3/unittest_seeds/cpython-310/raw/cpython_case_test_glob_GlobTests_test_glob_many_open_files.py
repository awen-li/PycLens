# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_many_open_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    depth = 30
    base = os.path.join(self.tempdir, 'deep')
    p = os.path.join(base, *['d'] * depth)
    os.makedirs(p)
    pattern = os.path.join(base, *['*'] * depth)
    iters = [glob.iglob(pattern, recursive=True) for j in range(100)]
    for it in iters:
        self.assertEqual(next(it), p)
    pattern = os.path.join(base, '**', 'd')
    iters = [glob.iglob(pattern, recursive=True) for j in range(100)]
    p = base
    for i in range(depth):
        p = os.path.join(p, 'd')
        for it in iters:
            self.assertEqual(next(it), p)
