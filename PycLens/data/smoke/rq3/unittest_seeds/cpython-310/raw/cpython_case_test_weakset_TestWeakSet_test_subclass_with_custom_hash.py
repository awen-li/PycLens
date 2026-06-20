# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_subclass_with_custom_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class H(WeakSet):

        def __hash__(self):
            return int(id(self) & 2147483647)
    s = H()
    f = set()
    f.add(s)
    self.assertIn(s, f)
    f.remove(s)
    f.add(s)
    f.discard(s)
