# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_resurrection_does_not_block_cleanup_of_other_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 100

    class A:

        def __init__(self):
            self.me = self

    class Z(A):

        def __del__(self):
            zs.append(self)
    zs = []

    def getstats():
        d = gc.get_stats()[-1]
        return (d['collected'], d['uncollectable'])
    gc.collect()
    gc.disable()
    (oldc, oldnc) = getstats()
    for i in range(N):
        A()
    t = gc.collect()
    (c, nc) = getstats()
    self.assertEqual(t, 2 * N)
    self.assertEqual(c - oldc, 2 * N)
    self.assertEqual(nc - oldnc, 0)
    (oldc, oldnc) = (c, nc)
    Z()
    t = gc.collect()
    (c, nc) = getstats()
    self.assertEqual(t, 0)
    self.assertEqual(c - oldc, 0)
    self.assertEqual(nc - oldnc, 0)
    (oldc, oldnc) = (c, nc)
    for i in range(N):
        A()
    Z()
    t = gc.collect()
    (c, nc) = getstats()
    self.assertEqual(t, 2 * N)
    self.assertEqual(c - oldc, 2 * N)
    self.assertEqual(nc - oldnc, 0)
    (oldc, oldnc) = (c, nc)
    zs.clear()
    t = gc.collect()
    (c, nc) = getstats()
    self.assertEqual(t, 4)
    self.assertEqual(c - oldc, 4)
    self.assertEqual(nc - oldnc, 0)
    gc.enable()
