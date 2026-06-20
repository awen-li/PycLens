# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b32hexencode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_cases = [(b'', b''), (b'\x00', b'00======'), (b'a', b'C4======'), (b'ab', b'C5H0===='), (b'abc', b'C5H66==='), (b'abcd', b'C5H66P0='), (b'abcde', b'C5H66P35')]
    for (to_encode, expected) in test_cases:
        with self.subTest(to_decode=to_encode):
            self.assertEqual(base64.b32hexencode(to_encode), expected)
