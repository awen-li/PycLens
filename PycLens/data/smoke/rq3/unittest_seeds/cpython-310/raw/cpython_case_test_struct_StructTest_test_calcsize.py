# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_calcsize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_size = {'b': 1, 'B': 1, 'h': 2, 'H': 2, 'i': 4, 'I': 4, 'l': 4, 'L': 4, 'q': 8, 'Q': 8}
    for (code, byteorder) in iter_integer_formats(('=', '<', '>', '!')):
        format = byteorder + code
        size = struct.calcsize(format)
        self.assertEqual(size, expected_size[code])
    native_pairs = ('bB', 'hH', 'iI', 'lL', 'nN', 'qQ')
    for format_pair in native_pairs:
        for byteorder in ('', '@'):
            signed_size = struct.calcsize(byteorder + format_pair[0])
            unsigned_size = struct.calcsize(byteorder + format_pair[1])
            self.assertEqual(signed_size, unsigned_size)
    self.assertEqual(struct.calcsize('b'), 1)
    self.assertLessEqual(2, struct.calcsize('h'))
    self.assertLessEqual(4, struct.calcsize('l'))
    self.assertLessEqual(struct.calcsize('h'), struct.calcsize('i'))
    self.assertLessEqual(struct.calcsize('i'), struct.calcsize('l'))
    self.assertLessEqual(8, struct.calcsize('q'))
    self.assertLessEqual(struct.calcsize('l'), struct.calcsize('q'))
    self.assertGreaterEqual(struct.calcsize('n'), struct.calcsize('i'))
    self.assertGreaterEqual(struct.calcsize('n'), struct.calcsize('P'))
