# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO()
    t = self.TextIOWrapper(raw, encoding='utf-8')
    with support.swap_attr(raw, 'name', t):
        try:
            repr(t)
        except RuntimeError:
            pass
