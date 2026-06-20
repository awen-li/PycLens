# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_disallow_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (algorithm, constructors) in self.constructors_to_test.items():
        if algorithm.startswith(('sha3_', 'shake', 'blake')):
            continue
        for constructor in constructors:
            try:
                h = constructor()
            except ValueError:
                continue
            with self.subTest(constructor=constructor):
                support.check_disallow_instantiation(self, type(h))
