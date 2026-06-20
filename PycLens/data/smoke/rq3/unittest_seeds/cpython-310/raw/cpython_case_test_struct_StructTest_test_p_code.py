# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_p_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (code, input, expected, expectedback) in [('p', b'abc', b'\x00', b''), ('1p', b'abc', b'\x00', b''), ('2p', b'abc', b'\x01a', b'a'), ('3p', b'abc', b'\x02ab', b'ab'), ('4p', b'abc', b'\x03abc', b'abc'), ('5p', b'abc', b'\x03abc\x00', b'abc'), ('6p', b'abc', b'\x03abc\x00\x00', b'abc'), ('1000p', b'x' * 1000, b'\xff' + b'x' * 999, b'x' * 255)]:
        got = struct.pack(code, input)
        self.assertEqual(got, expected)
        (got,) = struct.unpack(code, got)
        self.assertEqual(got, expectedback)
