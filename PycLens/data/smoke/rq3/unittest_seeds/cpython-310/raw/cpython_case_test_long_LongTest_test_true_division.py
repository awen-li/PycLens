# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_true_division

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    huge = 1 << 40000
    mhuge = -huge
    self.assertEqual(huge / huge, 1.0)
    self.assertEqual(mhuge / mhuge, 1.0)
    self.assertEqual(huge / mhuge, -1.0)
    self.assertEqual(mhuge / huge, -1.0)
    self.assertEqual(1 / huge, 0.0)
    self.assertEqual(1 / huge, 0.0)
    self.assertEqual(1 / mhuge, 0.0)
    self.assertEqual(1 / mhuge, 0.0)
    self.assertEqual((666 * huge + (huge >> 1)) / huge, 666.5)
    self.assertEqual((666 * mhuge + (mhuge >> 1)) / mhuge, 666.5)
    self.assertEqual((666 * huge + (huge >> 1)) / mhuge, -666.5)
    self.assertEqual((666 * mhuge + (mhuge >> 1)) / huge, -666.5)
    self.assertEqual(huge / (huge << 1), 0.5)
    self.assertEqual(1000000 * huge / huge, 1000000)
    namespace = {'huge': huge, 'mhuge': mhuge}
    for overflow in ['float(huge)', 'float(mhuge)', 'huge / 1', 'huge / 2', 'huge / -1', 'huge / -2', 'mhuge / 100', 'mhuge / 200']:
        self.assertRaises(OverflowError, eval, overflow, namespace)
    for underflow in ['1 / huge', '2 / huge', '-1 / huge', '-2 / huge', '100 / mhuge', '200 / mhuge']:
        result = eval(underflow, namespace)
        self.assertEqual(result, 0.0, 'expected underflow to 0 from %r' % underflow)
    for zero in ['huge / 0', 'mhuge / 0']:
        self.assertRaises(ZeroDivisionError, eval, zero, namespace)
