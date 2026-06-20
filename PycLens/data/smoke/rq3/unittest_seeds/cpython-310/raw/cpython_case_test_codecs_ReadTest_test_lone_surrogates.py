# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ReadTest_test_lone_surrogates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(UnicodeEncodeError, '\ud800'.encode, self.encoding)
    self.assertEqual('[\udc80]'.encode(self.encoding, 'backslashreplace'), '[\\udc80]'.encode(self.encoding))
    self.assertEqual('[\udc80]'.encode(self.encoding, 'namereplace'), '[\\udc80]'.encode(self.encoding))
    self.assertEqual('[\udc80]'.encode(self.encoding, 'xmlcharrefreplace'), '[&#56448;]'.encode(self.encoding))
    self.assertEqual('[\udc80]'.encode(self.encoding, 'ignore'), '[]'.encode(self.encoding))
    self.assertEqual('[\udc80]'.encode(self.encoding, 'replace'), '[?]'.encode(self.encoding))
    self.assertEqual('[\ud800\udc80]'.encode(self.encoding, 'ignore'), '[]'.encode(self.encoding))
    self.assertEqual('[\ud800\udc80]'.encode(self.encoding, 'replace'), '[??]'.encode(self.encoding))
    bom = ''.encode(self.encoding)
    for (before, after) in [('\U00010fff', 'A'), ('[', ']'), ('A', '\U00010fff')]:
        before_sequence = before.encode(self.encoding)[len(bom):]
        after_sequence = after.encode(self.encoding)[len(bom):]
        test_string = before + '\udc80' + after
        test_sequence = bom + before_sequence + self.ill_formed_sequence + after_sequence
        self.assertRaises(UnicodeDecodeError, test_sequence.decode, self.encoding)
        self.assertEqual(test_string.encode(self.encoding, 'surrogatepass'), test_sequence)
        self.assertEqual(test_sequence.decode(self.encoding, 'surrogatepass'), test_string)
        self.assertEqual(test_sequence.decode(self.encoding, 'ignore'), before + after)
        self.assertEqual(test_sequence.decode(self.encoding, 'replace'), before + self.ill_formed_sequence_replace + after)
        backslashreplace = ''.join(('\\x%02x' % b for b in self.ill_formed_sequence))
        self.assertEqual(test_sequence.decode(self.encoding, 'backslashreplace'), before + backslashreplace + after)
