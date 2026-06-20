# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_function_checksum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = []
    h = hashlib.sha1()
    for i in range(sys.maxunicode + 1):
        char = chr(i)
        data = [format(self.db.digit(char, -1), '.12g'), format(self.db.numeric(char, -1), '.12g'), format(self.db.decimal(char, -1), '.12g'), self.db.category(char), self.db.bidirectional(char), self.db.decomposition(char), str(self.db.mirrored(char)), str(self.db.combining(char))]
        h.update(''.join(data).encode('ascii'))
    result = h.hexdigest()
    self.assertEqual(result, self.expectedchecksum)
