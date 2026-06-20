# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF7Test_test_nonbmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('𐒠'.encode(self.encoding), b'+2AHcoA-')
    self.assertEqual('\ud801\udca0'.encode(self.encoding), b'+2AHcoA-')
    self.assertEqual(b'+2AHcoA-'.decode(self.encoding), '𐒠')
    self.assertEqual(b'+2AHcoA'.decode(self.encoding), '𐒠')
    self.assertEqual('€𐒠'.encode(self.encoding), b'+IKzYAdyg-')
    self.assertEqual(b'+IKzYAdyg-'.decode(self.encoding), '€𐒠')
    self.assertEqual(b'+IKzYAdyg'.decode(self.encoding), '€𐒠')
    self.assertEqual('€€𐒠'.encode(self.encoding), b'+IKwgrNgB3KA-')
    self.assertEqual(b'+IKwgrNgB3KA-'.decode(self.encoding), '€€𐒠')
    self.assertEqual(b'+IKwgrNgB3KA'.decode(self.encoding), '€€𐒠')
