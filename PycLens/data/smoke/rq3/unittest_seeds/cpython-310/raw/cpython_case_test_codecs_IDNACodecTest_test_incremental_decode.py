# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: IDNACodecTest_test_incremental_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(''.join(codecs.iterdecode((bytes([c]) for c in b'python.org'), 'idna')), 'python.org')
    self.assertEqual(''.join(codecs.iterdecode((bytes([c]) for c in b'python.org.'), 'idna')), 'python.org.')
    self.assertEqual(''.join(codecs.iterdecode((bytes([c]) for c in b'xn--pythn-mua.org.'), 'idna')), 'pythön.org.')
    self.assertEqual(''.join(codecs.iterdecode((bytes([c]) for c in b'xn--pythn-mua.org.'), 'idna')), 'pythön.org.')
    decoder = codecs.getincrementaldecoder('idna')()
    self.assertEqual(decoder.decode(b'xn--xam'), '')
    self.assertEqual(decoder.decode(b'ple-9ta.o'), 'äxample.')
    self.assertEqual(decoder.decode(b'rg'), '')
    self.assertEqual(decoder.decode(b'', True), 'org')
    decoder.reset()
    self.assertEqual(decoder.decode(b'xn--xam'), '')
    self.assertEqual(decoder.decode(b'ple-9ta.o'), 'äxample.')
    self.assertEqual(decoder.decode(b'rg.'), 'org.')
    self.assertEqual(decoder.decode(b'', True), '')
