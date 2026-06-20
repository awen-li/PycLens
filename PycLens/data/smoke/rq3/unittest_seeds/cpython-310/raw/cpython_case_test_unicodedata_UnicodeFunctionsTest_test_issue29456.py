# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_issue29456

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u1176_str_a = 'ᄀᅶᆨ'
    u1176_str_b = 'ᄀᅶᆨ'
    u11a7_str_a = '기ᆧ'
    u11a7_str_b = '기ᆧ'
    u11c3_str_a = '기ᇃ'
    u11c3_str_b = '기ᇃ'
    self.assertEqual(self.db.normalize('NFC', u1176_str_a), u1176_str_b)
    self.assertEqual(self.db.normalize('NFC', u11a7_str_a), u11a7_str_b)
    self.assertEqual(self.db.normalize('NFC', u11c3_str_a), u11c3_str_b)
