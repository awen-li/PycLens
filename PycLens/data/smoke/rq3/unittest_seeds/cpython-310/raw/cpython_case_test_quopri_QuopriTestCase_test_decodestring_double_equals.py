# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_quopri.py
# case: QuopriTestCase_test_decodestring_double_equals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (decoded_value, encoded_value) = (b'123=four', b'123==four')
    self.assertEqual(quopri.decodestring(encoded_value), decoded_value)
