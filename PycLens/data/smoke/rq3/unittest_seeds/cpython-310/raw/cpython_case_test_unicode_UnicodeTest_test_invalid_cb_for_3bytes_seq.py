# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_invalid_cb_for_3bytes_seq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    FFFD = '�'
    FFFDx2 = FFFD * 2
    sequences = [('E0 00', FFFD + '\x00'), ('E0 7F', FFFD + '\x7f'), ('E0 80', FFFDx2), ('E0 9F', FFFDx2), ('E0 C0', FFFDx2), ('E0 FF', FFFDx2), ('E0 A0 00', FFFD + '\x00'), ('E0 A0 7F', FFFD + '\x7f'), ('E0 A0 C0', FFFDx2), ('E0 A0 FF', FFFDx2), ('E0 BF 00', FFFD + '\x00'), ('E0 BF 7F', FFFD + '\x7f'), ('E0 BF C0', FFFDx2), ('E0 BF FF', FFFDx2), ('E1 00', FFFD + '\x00'), ('E1 7F', FFFD + '\x7f'), ('E1 C0', FFFDx2), ('E1 FF', FFFDx2), ('E1 80 00', FFFD + '\x00'), ('E1 80 7F', FFFD + '\x7f'), ('E1 80 C0', FFFDx2), ('E1 80 FF', FFFDx2), ('E1 BF 00', FFFD + '\x00'), ('E1 BF 7F', FFFD + '\x7f'), ('E1 BF C0', FFFDx2), ('E1 BF FF', FFFDx2), ('EC 00', FFFD + '\x00'), ('EC 7F', FFFD + '\x7f'), ('EC C0', FFFDx2), ('EC FF', FFFDx2), ('EC 80 00', FFFD + '\x00'), ('EC 80 7F', FFFD + '\x7f'), ('EC 80 C0', FFFDx2), ('EC 80 FF', FFFDx2), ('EC BF 00', FFFD + '\x00'), ('EC BF 7F', FFFD + '\x7f'), ('EC BF C0', FFFDx2), ('EC BF FF', FFFDx2), ('ED 00', FFFD + '\x00'), ('ED 7F', FFFD + '\x7f'), ('ED A0', FFFDx2), ('ED BF', FFFDx2), ('ED C0', FFFDx2), ('ED FF', FFFDx2), ('ED 80 00', FFFD + '\x00'), ('ED 80 7F', FFFD + '\x7f'), ('ED 80 C0', FFFDx2), ('ED 80 FF', FFFDx2), ('ED 9F 00', FFFD + '\x00'), ('ED 9F 7F', FFFD + '\x7f'), ('ED 9F C0', FFFDx2), ('ED 9F FF', FFFDx2), ('EE 00', FFFD + '\x00'), ('EE 7F', FFFD + '\x7f'), ('EE C0', FFFDx2), ('EE FF', FFFDx2), ('EE 80 00', FFFD + '\x00'), ('EE 80 7F', FFFD + '\x7f'), ('EE 80 C0', FFFDx2), ('EE 80 FF', FFFDx2), ('EE BF 00', FFFD + '\x00'), ('EE BF 7F', FFFD + '\x7f'), ('EE BF C0', FFFDx2), ('EE BF FF', FFFDx2), ('EF 00', FFFD + '\x00'), ('EF 7F', FFFD + '\x7f'), ('EF C0', FFFDx2), ('EF FF', FFFDx2), ('EF 80 00', FFFD + '\x00'), ('EF 80 7F', FFFD + '\x7f'), ('EF 80 C0', FFFDx2), ('EF 80 FF', FFFDx2), ('EF BF 00', FFFD + '\x00'), ('EF BF 7F', FFFD + '\x7f'), ('EF BF C0', FFFDx2), ('EF BF FF', FFFDx2)]
    for (seq, res) in sequences:
        self.assertCorrectUTF8Decoding(bytes.fromhex(seq), res, 'invalid continuation byte')
