# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_keyword_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(int('100', base=2), 4)
    with self.assertRaisesRegex(TypeError, 'keyword argument'):
        int(x=1.2)
    with self.assertRaisesRegex(TypeError, 'keyword argument'):
        int(x='100', base=2)
    self.assertRaises(TypeError, int, base=10)
    self.assertRaises(TypeError, int, base=0)
