# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_access_to_nonexistent_digit_0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Integer(int):

        def __new__(cls, value=0):
            self = int.__new__(cls, value)
            self.foo = 'foo'
            return self
    integers = [Integer(0) for i in range(1000)]
    for n in map(int, integers):
        self.assertEqual(n, 0)
