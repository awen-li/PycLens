# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestBytes_test_byte_content

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = [b'hello', b'andr\xe9']
    b = [b'hello', b'andr\xc3\xa9']
    unified = difflib.unified_diff
    context = difflib.context_diff
    check = self.check
    check(difflib.diff_bytes(unified, a, a))
    check(difflib.diff_bytes(unified, a, b))
    check(difflib.diff_bytes(unified, a, a, b'a', b'a'))
    check(difflib.diff_bytes(unified, a, b, b'a', b'b'))
    check(difflib.diff_bytes(unified, a, a, b'a', b'a', b'2005', b'2013'))
    check(difflib.diff_bytes(unified, a, b, b'a', b'b', b'2005', b'2013'))
    check(difflib.diff_bytes(context, a, a))
    check(difflib.diff_bytes(context, a, b))
    check(difflib.diff_bytes(context, a, a, b'a', b'a'))
    check(difflib.diff_bytes(context, a, b, b'a', b'b'))
    check(difflib.diff_bytes(context, a, a, b'a', b'a', b'2005', b'2013'))
    check(difflib.diff_bytes(context, a, b, b'a', b'b', b'2005', b'2013'))
