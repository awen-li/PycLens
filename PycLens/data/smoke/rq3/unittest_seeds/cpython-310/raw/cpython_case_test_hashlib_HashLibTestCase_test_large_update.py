# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_large_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    aas = b'a' * 128
    bees = b'b' * 127
    cees = b'c' * 126
    dees = b'd' * 2048
    for cons in self.hash_constructors:
        m1 = cons(usedforsecurity=False)
        m1.update(aas)
        m1.update(bees)
        m1.update(cees)
        m1.update(dees)
        if m1.name in self.shakes:
            args = (16,)
        else:
            args = ()
        m2 = cons(usedforsecurity=False)
        m2.update(aas + bees + cees + dees)
        self.assertEqual(m1.digest(*args), m2.digest(*args))
        m3 = cons(aas + bees + cees + dees, usedforsecurity=False)
        self.assertEqual(m1.digest(*args), m3.digest(*args))
        m4 = cons(aas + bees + cees, usedforsecurity=False)
        m4_digest = m4.digest(*args)
        m4_copy = m4.copy()
        m4_copy.update(dees)
        self.assertEqual(m1.digest(*args), m4_copy.digest(*args))
        self.assertEqual(m4.digest(*args), m4_digest)
