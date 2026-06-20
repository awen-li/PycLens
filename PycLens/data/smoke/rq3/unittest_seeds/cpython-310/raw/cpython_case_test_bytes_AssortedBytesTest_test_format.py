# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for b in (b'abc', bytearray(b'abc')):
        self.assertEqual(format(b), str(b))
        self.assertEqual(format(b, ''), str(b))
        with self.assertRaisesRegex(TypeError, '\\b%s\\b' % re.escape(type(b).__name__)):
            format(b, 's')
