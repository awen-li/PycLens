# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_unexpected_end_of_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sequences = ['C2', 'DF', 'E0 A0', 'E0 BF', 'E1 80', 'E1 BF', 'EC 80', 'EC BF', 'ED 80', 'ED 9F', 'EE 80', 'EE BF', 'EF 80', 'EF BF', 'F0 90', 'F0 BF', 'F0 90 80', 'F0 90 BF', 'F0 BF 80', 'F0 BF BF', 'F1 80', 'F1 BF', 'F1 80 80', 'F1 80 BF', 'F1 BF 80', 'F1 BF BF', 'F3 80', 'F3 BF', 'F3 80 80', 'F3 80 BF', 'F3 BF 80', 'F3 BF BF', 'F4 80', 'F4 8F', 'F4 80 80', 'F4 80 BF', 'F4 8F 80', 'F4 8F BF']
    FFFD = '�'
    for seq in sequences:
        self.assertCorrectUTF8Decoding(bytes.fromhex(seq), '�', 'unexpected end of data')
