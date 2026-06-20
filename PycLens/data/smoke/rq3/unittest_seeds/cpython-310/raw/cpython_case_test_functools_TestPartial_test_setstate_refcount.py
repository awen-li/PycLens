# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_setstate_refcount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadSequence:

        def __len__(self):
            return 4

        def __getitem__(self, key):
            if key == 0:
                return max
            elif key == 1:
                return tuple(range(1000000))
            elif key in (2, 3):
                return {}
            raise IndexError
    f = self.partial(object)
    self.assertRaises(TypeError, f.__setstate__, BadSequence())
