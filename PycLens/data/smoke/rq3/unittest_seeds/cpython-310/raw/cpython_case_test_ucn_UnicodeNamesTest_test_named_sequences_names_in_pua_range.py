# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_named_sequences_names_in_pua_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cp in range(983296, 987135):
        with self.assertRaises(ValueError) as cm:
            unicodedata.name(chr(cp))
        self.assertEqual(str(cm.exception), 'no such name')
