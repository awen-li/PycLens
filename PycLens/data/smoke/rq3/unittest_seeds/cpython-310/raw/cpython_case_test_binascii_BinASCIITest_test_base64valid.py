# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_base64valid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    MAX_BASE64 = 57
    lines = []
    for i in range(0, len(self.rawdata), MAX_BASE64):
        b = self.type2test(self.rawdata[i:i + MAX_BASE64])
        a = binascii.b2a_base64(b)
        lines.append(a)
    res = bytes()
    for line in lines:
        a = self.type2test(line)
        b = binascii.a2b_base64(a)
        res += b
    self.assertEqual(res, self.rawdata)
