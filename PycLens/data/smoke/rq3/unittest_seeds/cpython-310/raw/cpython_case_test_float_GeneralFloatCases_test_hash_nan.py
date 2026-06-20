# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_hash_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value = float('nan')
    self.assertEqual(hash(value), object.__hash__(value))

    class H:

        def __hash__(self):
            return 42

    class F(float, H):
        pass
    value = F('nan')
    self.assertEqual(hash(value), object.__hash__(value))
