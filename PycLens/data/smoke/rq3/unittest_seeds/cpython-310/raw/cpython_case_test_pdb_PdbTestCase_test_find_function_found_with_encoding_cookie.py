# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_find_function_found_with_encoding_cookie

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._assert_find_function('# coding: iso-8859-15\ndef foo():\n    pass\n\ndef bœr():\n    pass\n\ndef quux():\n    pass\n'.encode('iso-8859-15'), 'bœr', ('bœr', 5))
