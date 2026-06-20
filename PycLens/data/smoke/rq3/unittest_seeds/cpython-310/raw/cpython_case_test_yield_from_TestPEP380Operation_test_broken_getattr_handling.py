# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_broken_getattr_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Broken:

        def __iter__(self):
            return self

        def __next__(self):
            return 1

        def __getattr__(self, attr):
            1 / 0

    def g():
        yield from Broken()
    with self.assertRaises(ZeroDivisionError):
        gi = g()
        self.assertEqual(next(gi), 1)
        gi.send(1)
    with self.assertRaises(ZeroDivisionError):
        gi = g()
        self.assertEqual(next(gi), 1)
        gi.throw(AttributeError)
    with support.catch_unraisable_exception() as cm:
        gi = g()
        self.assertEqual(next(gi), 1)
        gi.close()
        self.assertEqual(ZeroDivisionError, cm.unraisable.exc_type)
