# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_invalid_cb_for_2bytes_seq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    FFFD = '�'
    FFFDx2 = FFFD * 2
    sequences = [('C2 00', FFFD + '\x00'), ('C2 7F', FFFD + '\x7f'), ('C2 C0', FFFDx2), ('C2 FF', FFFDx2), ('DF 00', FFFD + '\x00'), ('DF 7F', FFFD + '\x7f'), ('DF C0', FFFDx2), ('DF FF', FFFDx2)]
    for (seq, res) in sequences:
        self.assertCorrectUTF8Decoding(bytes.fromhex(seq), res, 'invalid continuation byte')
