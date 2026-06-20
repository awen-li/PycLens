# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_246

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(x):
        match x:
            case [a, b, c, d, e, f, g, h, i, 9] | [h, g, i, a, b, d, e, c, f, 10] | [g, b, a, c, d, -5, e, h, i, f] | [-1, d, f, b, g, e, i, a, h, c]:
                w = 0
        out = locals()
        del out['x']
        return out
    alts = [dict(a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7, i=8, w=0), dict(h=1, g=2, i=3, a=4, b=5, d=6, e=7, c=8, f=9, w=0), dict(g=0, b=-1, a=-2, c=-3, d=-4, e=-6, h=-7, i=-8, f=-9, w=0), dict(d=-2, f=-3, b=-4, g=-5, e=-6, i=-7, a=-8, h=-9, c=-10, w=0), dict()]
    self.assertEqual(f(range(10)), alts[0])
    self.assertEqual(f(range(1, 11)), alts[1])
    self.assertEqual(f(range(0, -10, -1)), alts[2])
    self.assertEqual(f(range(-1, -11, -1)), alts[3])
    self.assertEqual(f(range(10, 20)), alts[4])
