# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_large_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoded = b'01234567' * (size // 8 - 1) + b'\x85\x86\xea\xeb\xec\xef\xfc\xfd\xfe\xff'
    self.assertEqual(len(encoded), size + 2)
    decoded = codecs.code_page_decode(932, encoded, 'surrogateescape', True)
    self.assertEqual(decoded[1], len(encoded))
    del encoded
    self.assertEqual(len(decoded[0]), decoded[1])
    self.assertEqual(decoded[0][:10], '0123456701')
    self.assertEqual(decoded[0][-20:], '6701234567\udc85\udc86\udcea\udceb\udcec\udcef\udcfc\udcfd\udcfe\udcff')
