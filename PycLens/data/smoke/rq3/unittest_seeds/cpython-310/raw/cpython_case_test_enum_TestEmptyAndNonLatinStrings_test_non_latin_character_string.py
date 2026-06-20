# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEmptyAndNonLatinStrings_test_non_latin_character_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    greek_abc = Enum('greek_abc', ('α', 'B', 'C'))
    item = getattr(greek_abc, 'α')
    self.assertEqual(item.value, 1)
