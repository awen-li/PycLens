# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_boom2_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Boom2_New(object):

        def __init__(self):
            self.x = 0

        def __getattr__(self, someattribute):
            self.x += 1
            if self.x > 1:
                del self.attr
            raise AttributeError
    a = Boom2_New()
    b = Boom2_New()
    a.attr = b
    b.attr = a
    gc.collect()
    garbagelen = len(gc.garbage)
    del a, b
    self.assertEqual(gc.collect(), 4)
    self.assertEqual(len(gc.garbage), garbagelen)
