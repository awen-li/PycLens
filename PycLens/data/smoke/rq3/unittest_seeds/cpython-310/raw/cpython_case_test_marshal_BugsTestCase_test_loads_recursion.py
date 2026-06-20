# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_loads_recursion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def run_tests(N, check):
        check(b')\x01' * N + b'N')
        check(b'(\x01\x00\x00\x00' * N + b'N')
        check(b'[\x01\x00\x00\x00' * N + b'N')
        check(b'{N' * N + b'N' + b'0' * N)
        check(b'>\x01\x00\x00\x00' * N + b'N')
    run_tests(100, marshal.loads)

    def check(s):
        self.assertRaises(ValueError, marshal.loads, s)
    run_tests(2 ** 20, check)
