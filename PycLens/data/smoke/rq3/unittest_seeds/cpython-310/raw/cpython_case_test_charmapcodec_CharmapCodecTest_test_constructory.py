# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_charmapcodec.py
# case: CharmapCodecTest_test_constructory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(b'ydef', codecname), 'def')
    self.assertEqual(str(b'defy', codecname), 'def')
    self.assertEqual(str(b'dyf', codecname), 'df')
    self.assertEqual(str(b'dyfy', codecname), 'df')
