# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b32hexdecode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_cases = [(b'', b'', False), (b'00======', b'\x00', False), (b'C4======', b'a', False), (b'C5H0====', b'ab', False), (b'C5H66===', b'abc', False), (b'C5H66P0=', b'abcd', False), (b'C5H66P35', b'abcde', False), (b'', b'', True), (b'00======', b'\x00', True), (b'C4======', b'a', True), (b'C5H0====', b'ab', True), (b'C5H66===', b'abc', True), (b'C5H66P0=', b'abcd', True), (b'C5H66P35', b'abcde', True), (b'c4======', b'a', True), (b'c5h0====', b'ab', True), (b'c5h66===', b'abc', True), (b'c5h66p0=', b'abcd', True), (b'c5h66p35', b'abcde', True)]
    for (to_decode, expected, casefold) in test_cases:
        with self.subTest(to_decode=to_decode, casefold=casefold):
            self.assertEqual(base64.b32hexdecode(to_decode, casefold), expected)
            self.assertEqual(base64.b32hexdecode(to_decode.decode('ascii'), casefold), expected)
