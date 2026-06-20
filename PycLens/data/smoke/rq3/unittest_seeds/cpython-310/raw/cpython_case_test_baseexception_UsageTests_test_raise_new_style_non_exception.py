# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_baseexception.py
# case: UsageTests_test_raise_new_style_non_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NewStyleClass(object):
        pass
    self.raise_fails(NewStyleClass)
    self.raise_fails(NewStyleClass())
