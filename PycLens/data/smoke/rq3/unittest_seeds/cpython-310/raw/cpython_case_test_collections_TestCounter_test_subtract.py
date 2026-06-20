# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_subtract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = Counter(a=-5, b=0, c=5, d=10, e=15, g=40)
    c.subtract(a=1, b=2, c=-3, d=10, e=20, f=30, h=-50)
    self.assertEqual(c, Counter(a=-6, b=-2, c=8, d=0, e=-5, f=-30, g=40, h=50))
    c = Counter(a=-5, b=0, c=5, d=10, e=15, g=40)
    c.subtract(Counter(a=1, b=2, c=-3, d=10, e=20, f=30, h=-50))
    self.assertEqual(c, Counter(a=-6, b=-2, c=8, d=0, e=-5, f=-30, g=40, h=50))
    c = Counter('aaabbcd')
    c.subtract('aaaabbcce')
    self.assertEqual(c, Counter(a=-1, b=0, c=-1, d=1, e=-1))
    c = Counter()
    c.subtract(self=42)
    self.assertEqual(list(c.items()), [('self', -42)])
    c = Counter()
    c.subtract(iterable=42)
    self.assertEqual(list(c.items()), [('iterable', -42)])
    self.assertRaises(TypeError, Counter().subtract, 42)
    self.assertRaises(TypeError, Counter().subtract, {}, {})
    self.assertRaises(TypeError, Counter.subtract)
