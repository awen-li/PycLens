# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_base64invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    MAX_BASE64 = 57
    lines = []
    for i in range(0, len(self.data), MAX_BASE64):
        b = self.type2test(self.rawdata[i:i + MAX_BASE64])
        a = binascii.b2a_base64(b)
        lines.append(a)
    fillers = bytearray()
    valid = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
    for i in range(256):
        if i not in valid:
            fillers.append(i)

    def addnoise(line):
        noise = fillers
        ratio = len(line) // len(noise)
        res = bytearray()
        while line and noise:
            if len(line) // len(noise) > ratio:
                (c, line) = (line[0], line[1:])
            else:
                (c, noise) = (noise[0], noise[1:])
            res.append(c)
        return res + noise + line
    res = bytearray()
    for line in map(addnoise, lines):
        a = self.type2test(line)
        b = binascii.a2b_base64(a)
        res += b
    self.assertEqual(res, self.rawdata)
    self.assertEqual(binascii.a2b_base64(self.type2test(fillers)), b'')
