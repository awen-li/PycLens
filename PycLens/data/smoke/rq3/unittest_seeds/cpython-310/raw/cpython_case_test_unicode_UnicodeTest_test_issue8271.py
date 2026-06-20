# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_issue8271

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    FFFD = '�'
    sequences = [(b'\x80', FFFD), (b'\x80\x80', FFFD * 2), (b'\xc0', FFFD), (b'\xc0\xc0', FFFD * 2), (b'\xc1', FFFD), (b'\xc1\xc0', FFFD * 2), (b'\xc0\xc1', FFFD * 2), (b'\xc2', FFFD), (b'\xc2\xc2', FFFD * 2), (b'\xc2\xc2\xc2', FFFD * 3), (b'\xc2A', FFFD + 'A'), (b'\xe1', FFFD), (b'\xe1\xe1', FFFD * 2), (b'\xe1\xe1\xe1', FFFD * 3), (b'\xe1\xe1\xe1\xe1', FFFD * 4), (b'\xe1\x80', FFFD), (b'\xe1A', FFFD + 'A'), (b'\xe1A\x80', FFFD + 'A' + FFFD), (b'\xe1AA', FFFD + 'AA'), (b'\xe1\x80A', FFFD + 'A'), (b'\xe1\x80\xe1A', FFFD * 2 + 'A'), (b'\xe1A\xe1\x80', FFFD + 'A' + FFFD), (b'\xf1', FFFD), (b'\xf1\xf1', FFFD * 2), (b'\xf1\xf1\xf1', FFFD * 3), (b'\xf1\xf1\xf1\xf1', FFFD * 4), (b'\xf1\xf1\xf1\xf1\xf1', FFFD * 5), (b'\xf1\x80', FFFD), (b'\xf1\x80\x80', FFFD), (b'\xf1\x80A', FFFD + 'A'), (b'\xf1\x80AA', FFFD + 'AA'), (b'\xf1\x80\x80A', FFFD + 'A'), (b'\xf1A\x80', FFFD + 'A' + FFFD), (b'\xf1A\x80\x80', FFFD + 'A' + FFFD * 2), (b'\xf1A\x80A', FFFD + 'A' + FFFD + 'A'), (b'\xf1AA\x80', FFFD + 'AA' + FFFD), (b'\xf1A\xf1\x80', FFFD + 'A' + FFFD), (b'\xf1A\x80\xf1', FFFD + 'A' + FFFD * 2), (b'\xf1\xf1\x80A', FFFD * 2 + 'A'), (b'\xf1A\xf1\xf1', FFFD + 'A' + FFFD * 2), (b'\xf5', FFFD), (b'\xf5\xf5', FFFD * 2), (b'\xf5\x80', FFFD * 2), (b'\xf5\x80\x80', FFFD * 3), (b'\xf5\x80\x80\x80', FFFD * 4), (b'\xf5\x80A', FFFD * 2 + 'A'), (b'\xf5\x80A\xf5', FFFD * 2 + 'A' + FFFD), (b'\xf5A\x80\x80A', FFFD + 'A' + FFFD * 2 + 'A'), (b'\xf8', FFFD), (b'\xf8\xf8', FFFD * 2), (b'\xf8\x80', FFFD * 2), (b'\xf8\x80A', FFFD * 2 + 'A'), (b'\xf8\x80\x80\x80\x80', FFFD * 5), (b'\xfc', FFFD), (b'\xfc\xfc', FFFD * 2), (b'\xfc\x80\x80', FFFD * 3), (b'\xfc\x80\x80\x80\x80\x80', FFFD * 6), (b'\xfe', FFFD), (b'\xfe\x80\x80', FFFD * 3), (b'\xf1\x80ABC', '�ABC'), (b'\xf1\x80\xffBC', '��BC'), (b'\xf1\x80\xc2\x81C', '�\x81C'), (b'a\xf1\x80\x80\xe1\x80\xc2b\x80c\x80\xbfd', 'a���b�c��d')]
    for (n, (seq, res)) in enumerate(sequences):
        self.assertRaises(UnicodeDecodeError, seq.decode, 'utf-8', 'strict')
        self.assertEqual(seq.decode('utf-8', 'replace'), res)
        self.assertEqual((seq + b'b').decode('utf-8', 'replace'), res + 'b')
        self.assertEqual(seq.decode('utf-8', 'ignore'), res.replace('�', ''))
