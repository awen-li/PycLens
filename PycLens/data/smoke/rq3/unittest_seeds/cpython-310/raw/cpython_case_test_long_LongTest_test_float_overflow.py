# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_float_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (-2.0, -1.0, 0.0, 1.0, 2.0):
        self.assertEqual(float(int(x)), x)
    shuge = '12345' * 120
    huge = 1 << 30000
    mhuge = -huge
    namespace = {'huge': huge, 'mhuge': mhuge, 'shuge': shuge, 'math': math}
    for test in ['float(huge)', 'float(mhuge)', 'complex(huge)', 'complex(mhuge)', 'complex(huge, 1)', 'complex(mhuge, 1)', 'complex(1, huge)', 'complex(1, mhuge)', '1. + huge', 'huge + 1.', '1. + mhuge', 'mhuge + 1.', '1. - huge', 'huge - 1.', '1. - mhuge', 'mhuge - 1.', '1. * huge', 'huge * 1.', '1. * mhuge', 'mhuge * 1.', '1. // huge', 'huge // 1.', '1. // mhuge', 'mhuge // 1.', '1. / huge', 'huge / 1.', '1. / mhuge', 'mhuge / 1.', '1. ** huge', 'huge ** 1.', '1. ** mhuge', 'mhuge ** 1.', 'math.sin(huge)', 'math.sin(mhuge)', 'math.sqrt(huge)', 'math.sqrt(mhuge)']:
        self.assertRaises(OverflowError, eval, test, namespace)
    self.assertNotEqual(float(shuge), int(shuge), 'float(shuge) should not equal int(shuge)')
