# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_putenv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        os.putenv('FRUIT\x00VEGETABLE', 'cabbage')
    with self.assertRaises(ValueError):
        os.putenv(b'FRUIT\x00VEGETABLE', b'cabbage')
    with self.assertRaises(ValueError):
        os.putenv('FRUIT', 'orange\x00VEGETABLE=cabbage')
    with self.assertRaises(ValueError):
        os.putenv(b'FRUIT', b'orange\x00VEGETABLE=cabbage')
    with self.assertRaises(ValueError):
        os.putenv('FRUIT=ORANGE', 'lemon')
    with self.assertRaises(ValueError):
        os.putenv(b'FRUIT=ORANGE', b'lemon')
