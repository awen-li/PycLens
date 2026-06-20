# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEmptyAndNonLatinStrings_test_non_latin_number_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hebrew_123 = Enum('hebrew_123', ('א', '2', '3'))
    item = getattr(hebrew_123, 'א')
    self.assertEqual(item.value, 1)
