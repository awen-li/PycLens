# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUStdIOTest_test_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sys.stdin = FakeIO(plaintext.decode('ascii'))
    sys.stdout = FakeIO()
    uu.encode('-', '-', 't1', 438)
    self.assertEqual(sys.stdout.getvalue(), encodedtextwrapped(438, 't1').decode('ascii'))
