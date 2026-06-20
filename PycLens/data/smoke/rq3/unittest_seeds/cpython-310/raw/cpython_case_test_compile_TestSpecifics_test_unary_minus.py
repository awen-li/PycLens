# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_unary_minus

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.maxsize == 2147483647:
        all_one_bits = '0xffffffff'
        self.assertEqual(eval(all_one_bits), 4294967295)
        self.assertEqual(eval('-' + all_one_bits), -4294967295)
    elif sys.maxsize == 9223372036854775807:
        all_one_bits = '0xffffffffffffffff'
        self.assertEqual(eval(all_one_bits), 18446744073709551615)
        self.assertEqual(eval('-' + all_one_bits), -18446744073709551615)
    else:
        self.fail('How many bits *does* this machine have???')
    self.assertIsInstance(eval('%s' % (-sys.maxsize - 1)), int)
    self.assertIsInstance(eval('%s' % (-sys.maxsize - 2)), int)
