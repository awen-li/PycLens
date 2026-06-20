# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_zip_longest_bad_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exception = TypeError()

    class BadIterable:

        def __iter__(self):
            raise exception
    with self.assertRaises(TypeError) as cm:
        zip_longest(BadIterable())
    self.assertIs(cm.exception, exception)
