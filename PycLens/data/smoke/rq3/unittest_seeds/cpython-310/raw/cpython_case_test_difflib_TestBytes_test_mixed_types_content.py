# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestBytes_test_mixed_types_content

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = [b'hello']
    b = ['hello']
    unified = difflib.unified_diff
    context = difflib.context_diff
    expect = "lines to compare must be str, not bytes (b'hello')"
    self._assert_type_error(expect, unified, a, b)
    self._assert_type_error(expect, unified, b, a)
    self._assert_type_error(expect, context, a, b)
    self._assert_type_error(expect, context, b, a)
    expect = "all arguments must be bytes, not str ('hello')"
    self._assert_type_error(expect, difflib.diff_bytes, unified, a, b)
    self._assert_type_error(expect, difflib.diff_bytes, unified, b, a)
    self._assert_type_error(expect, difflib.diff_bytes, context, a, b)
    self._assert_type_error(expect, difflib.diff_bytes, context, b, a)
