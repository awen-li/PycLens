# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_weakref_segfault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import weakref

    class Provoker:

        def __init__(self, referrent):
            self.ref = weakref.ref(referrent)

        def __del__(self):
            x = self.ref()

    class Oops(object):
        pass
    o = Oops()
    o.whatever = Provoker(o)
    del o
