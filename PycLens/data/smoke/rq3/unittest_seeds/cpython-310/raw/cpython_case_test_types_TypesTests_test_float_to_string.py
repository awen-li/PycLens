# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_float_to_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(f, result):
        self.assertEqual(f.__format__('e'), result)
        self.assertEqual('%e' % f, result)
    for i in range(-99, 100):
        test(float('1.5e' + str(i)), '1.500000e{0:+03d}'.format(i))
    self.assertEqual(1.5e+100.__format__('e'), '1.500000e+100')
    self.assertEqual('%e' % 1.5e+100, '1.500000e+100')
    self.assertEqual(1.5e+101.__format__('e'), '1.500000e+101')
    self.assertEqual('%e' % 1.5e+101, '1.500000e+101')
    self.assertEqual(1.5e-100.__format__('e'), '1.500000e-100')
    self.assertEqual('%e' % 1.5e-100, '1.500000e-100')
    self.assertEqual(1.5e-101.__format__('e'), '1.500000e-101')
    self.assertEqual('%e' % 1.5e-101, '1.500000e-101')
    self.assertEqual('%g' % 1.0, '1')
    self.assertEqual('%#g' % 1.0, '1.00000')
