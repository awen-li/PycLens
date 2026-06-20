# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_iter_function_concealing_reentrant_exhaustion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    HAS_MORE = 1
    NO_MORE = 2

    def exhaust(iterator):
        """Exhaust an iterator without raising StopIteration."""
        list(iterator)

    def spam():
        if spam.is_recursive_call:
            return NO_MORE
        spam.is_recursive_call = True
        exhaust(spam.iterator)
        return HAS_MORE
    spam.is_recursive_call = False
    spam.iterator = iter(spam, NO_MORE)
    with self.assertRaises(StopIteration):
        next(spam.iterator)
