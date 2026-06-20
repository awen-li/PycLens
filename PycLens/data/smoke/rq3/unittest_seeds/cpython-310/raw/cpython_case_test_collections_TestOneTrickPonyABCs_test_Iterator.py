# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_samples = [None, 42, 3.14, 1j, b'', '', (), [], {}, set()]
    for x in non_samples:
        self.assertNotIsInstance(x, Iterator)
        self.assertFalse(issubclass(type(x), Iterator), repr(type(x)))
    samples = [iter(bytes()), iter(str()), iter(tuple()), iter(list()), iter(dict()), iter(set()), iter(frozenset()), iter(dict().keys()), iter(dict().items()), iter(dict().values()), _test_gen(), (x for x in [])]
    for x in samples:
        self.assertIsInstance(x, Iterator)
        self.assertTrue(issubclass(type(x), Iterator), repr(type(x)))
    self.validate_abstract_methods(Iterator, '__next__', '__iter__')

    class NextOnly:

        def __next__(self):
            yield 1
            return
    self.assertNotIsInstance(NextOnly(), Iterator)
