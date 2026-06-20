# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_new_features

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [('c', b'a', b'a', b'a', 0), ('xc', b'a', b'\x00a', b'\x00a', 0), ('cx', b'a', b'a\x00', b'a\x00', 0), ('s', b'a', b'a', b'a', 0), ('0s', b'helloworld', b'', b'', 1), ('1s', b'helloworld', b'h', b'h', 1), ('9s', b'helloworld', b'helloworl', b'helloworl', 1), ('10s', b'helloworld', b'helloworld', b'helloworld', 0), ('11s', b'helloworld', b'helloworld\x00', b'helloworld\x00', 1), ('20s', b'helloworld', b'helloworld' + 10 * b'\x00', b'helloworld' + 10 * b'\x00', 1), ('b', 7, b'\x07', b'\x07', 0), ('b', -7, b'\xf9', b'\xf9', 0), ('B', 7, b'\x07', b'\x07', 0), ('B', 249, b'\xf9', b'\xf9', 0), ('h', 700, b'\x02\xbc', b'\xbc\x02', 0), ('h', -700, b'\xfdD', b'D\xfd', 0), ('H', 700, b'\x02\xbc', b'\xbc\x02', 0), ('H', 65536 - 700, b'\xfdD', b'D\xfd', 0), ('i', 70000000, b'\x04,\x1d\x80', b'\x80\x1d,\x04', 0), ('i', -70000000, b'\xfb\xd3\xe2\x80', b'\x80\xe2\xd3\xfb', 0), ('I', 70000000, b'\x04,\x1d\x80', b'\x80\x1d,\x04', 0), ('I', 4294967296 - 70000000, b'\xfb\xd3\xe2\x80', b'\x80\xe2\xd3\xfb', 0), ('l', 70000000, b'\x04,\x1d\x80', b'\x80\x1d,\x04', 0), ('l', -70000000, b'\xfb\xd3\xe2\x80', b'\x80\xe2\xd3\xfb', 0), ('L', 70000000, b'\x04,\x1d\x80', b'\x80\x1d,\x04', 0), ('L', 4294967296 - 70000000, b'\xfb\xd3\xe2\x80', b'\x80\xe2\xd3\xfb', 0), ('f', 2.0, b'@\x00\x00\x00', b'\x00\x00\x00@', 0), ('d', 2.0, b'@\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00@', 0), ('f', -2.0, b'\xc0\x00\x00\x00', b'\x00\x00\x00\xc0', 0), ('d', -2.0, b'\xc0\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\xc0', 0), ('?', 0, b'\x00', b'\x00', 0), ('?', 3, b'\x01', b'\x01', 1), ('?', True, b'\x01', b'\x01', 0), ('?', [], b'\x00', b'\x00', 1), ('?', (1,), b'\x01', b'\x01', 1)]
    for (fmt, arg, big, lil, asy) in tests:
        for (xfmt, exp) in [('>' + fmt, big), ('!' + fmt, big), ('<' + fmt, lil), ('=' + fmt, ISBIGENDIAN and big or lil)]:
            res = struct.pack(xfmt, arg)
            self.assertEqual(res, exp)
            self.assertEqual(struct.calcsize(xfmt), len(res))
            rev = struct.unpack(xfmt, res)[0]
            if rev != arg:
                self.assertTrue(asy)
