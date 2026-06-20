# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestBytes_test_mixed_types_dates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = [b'foo\n']
    b = [b'bar\n']
    datea = '1 fév'
    dateb = '3 fév'
    self._assert_type_error("all arguments must be bytes, not str ('1 fév')", difflib.diff_bytes, difflib.unified_diff, a, b, b'a', b'b', datea, dateb)
    a = ['foo\n']
    b = ['bar\n']
    list(difflib.unified_diff(a, b, 'a', 'b', datea, dateb))
