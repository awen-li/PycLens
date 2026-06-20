# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: IsShareableTests_test_not_shareable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Cheese:

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    class SubBytes(bytes):
        """A subclass of a shareable type."""
    not_shareables = [True, False, NotImplemented, ..., type, object, object(), Exception(), 100.0, Cheese, Cheese('Wensleydale'), SubBytes(b'spam')]
    for obj in not_shareables:
        with self.subTest(repr(obj)):
            self.assertFalse(interpreters.is_shareable(obj))
