# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_selectors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import sys, time
    c = sys.path[0]
    x = time.time()
    x = sys.modules['time'].time()
    a = '01234'
    c = a[0]
    c = a[-1]
    s = a[0:5]
    s = a[:5]
    s = a[0:]
    s = a[:]
    s = a[-5:]
    s = a[:-1]
    s = a[-4:-3]
    d = {}
    d[1] = 1
    d[1,] = 2
    d[1, 2] = 3
    d[1, 2, 3] = 4
    L = list(d)
    L.sort(key=lambda x: (type(x).__name__, x))
    self.assertEqual(str(L), '[1, (1,), (1, 2), (1, 2, 3)]')
