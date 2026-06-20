# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestTypeErrors_test_accepts_positional_subpatterns_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = range(10)
    y = None
    with self.assertRaises(TypeError):
        match x:
            case range(10):
                y = 0
    self.assertEqual(x, range(10))
    self.assertIs(y, None)
