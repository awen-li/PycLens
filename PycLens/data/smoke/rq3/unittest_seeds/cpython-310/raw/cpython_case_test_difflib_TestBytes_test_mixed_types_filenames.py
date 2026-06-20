# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestBytes_test_mixed_types_filenames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ['hello\n']
    b = ['ohell\n']
    fna = b'ol\xe9.txt'
    fnb = b'ol\xc3a9.txt'
    self._assert_type_error("all arguments must be str, not: b'ol\\xe9.txt'", difflib.unified_diff, a, b, fna, fnb)
