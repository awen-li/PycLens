# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Callable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_samples = [None, 42, 3.14, 1j, '', b'', (), [], {}, set(), _test_gen(), (x for x in [])]
    for x in non_samples:
        self.assertNotIsInstance(x, Callable)
        self.assertFalse(issubclass(type(x), Callable), repr(type(x)))
    samples = [lambda : None, type, int, object, len, list.append, [].append]
    for x in samples:
        self.assertIsInstance(x, Callable)
        self.assertTrue(issubclass(type(x), Callable), repr(type(x)))
    self.validate_abstract_methods(Callable, '__call__')
    self.validate_isinstance(Callable, '__call__')
