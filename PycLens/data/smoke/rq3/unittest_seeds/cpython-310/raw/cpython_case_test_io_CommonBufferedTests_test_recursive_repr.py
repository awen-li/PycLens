# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()
    b = self.tp(raw)
    with support.swap_attr(raw, 'name', b):
        try:
            repr(b)
        except RuntimeError:
            pass
