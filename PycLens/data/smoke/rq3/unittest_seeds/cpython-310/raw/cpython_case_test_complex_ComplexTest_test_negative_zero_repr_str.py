# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_negative_zero_repr_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(v, expected, test_fn=self.assertEqual):
        test_fn(repr(v), expected)
        test_fn(str(v), expected)
    test(complex(0.0, 1.0), '1j')
    test(complex(-0.0, 1.0), '(-0+1j)')
    test(complex(0.0, -1.0), '-1j')
    test(complex(-0.0, -1.0), '(-0-1j)')
    test(complex(0.0, 0.0), '0j')
    test(complex(0.0, -0.0), '-0j')
    test(complex(-0.0, 0.0), '(-0+0j)')
    test(complex(-0.0, -0.0), '(-0-0j)')
