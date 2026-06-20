# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_repr_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(v, expected, test_fn=self.assertEqual):
        test_fn(repr(v), expected)
        test_fn(str(v), expected)
    test(1 + 6j, '(1+6j)')
    test(1 - 6j, '(1-6j)')
    test(-(1 + 0j), '(-1+-0j)', test_fn=self.assertNotEqual)
    test(complex(1.0, INF), '(1+infj)')
    test(complex(1.0, -INF), '(1-infj)')
    test(complex(INF, 1), '(inf+1j)')
    test(complex(-INF, INF), '(-inf+infj)')
    test(complex(NAN, 1), '(nan+1j)')
    test(complex(1, NAN), '(1+nanj)')
    test(complex(NAN, NAN), '(nan+nanj)')
    test(complex(0, INF), 'infj')
    test(complex(0, -INF), '-infj')
    test(complex(0, NAN), 'nanj')
    self.assertEqual(1 - 6j, complex(repr(1 - 6j)))
    self.assertEqual(1 + 6j, complex(repr(1 + 6j)))
    self.assertEqual(-6j, complex(repr(-6j)))
    self.assertEqual(6j, complex(repr(6j)))
