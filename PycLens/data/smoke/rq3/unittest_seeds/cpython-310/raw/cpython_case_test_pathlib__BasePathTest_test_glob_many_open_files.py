# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_glob_many_open_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    depth = 30
    P = self.cls
    base = P(BASE) / 'deep'
    p = P(base, *['d'] * depth)
    p.mkdir(parents=True)
    pattern = '/'.join(['*'] * depth)
    iters = [base.glob(pattern) for j in range(100)]
    for it in iters:
        self.assertEqual(next(it), p)
    iters = [base.rglob('d') for j in range(100)]
    p = base
    for i in range(depth):
        p = p / 'd'
        for it in iters:
            self.assertEqual(next(it), p)
