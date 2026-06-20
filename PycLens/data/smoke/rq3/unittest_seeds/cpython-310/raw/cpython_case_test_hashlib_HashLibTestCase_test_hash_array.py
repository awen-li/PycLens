# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_hash_array

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('b', range(10))
    for cons in self.hash_constructors:
        c = cons(a, usedforsecurity=False)
        if c.name in self.shakes:
            c.hexdigest(16)
        else:
            c.hexdigest()
