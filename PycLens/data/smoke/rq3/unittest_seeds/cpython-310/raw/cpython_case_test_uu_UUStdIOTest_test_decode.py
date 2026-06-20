# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUStdIOTest_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sys.stdin = FakeIO(encodedtextwrapped(438, 't1').decode('ascii'))
    sys.stdout = FakeIO()
    uu.decode('-', '-')
    stdout = sys.stdout
    sys.stdout = self.stdout
    sys.stdin = self.stdin
    self.assertEqual(stdout.getvalue(), plaintext.decode('ascii'))
