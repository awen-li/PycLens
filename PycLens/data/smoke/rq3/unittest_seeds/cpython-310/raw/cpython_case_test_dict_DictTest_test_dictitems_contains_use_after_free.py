# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_dictitems_contains_use_after_free

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __eq__(self, other):
            d.clear()
            return NotImplemented
    d = {0: set()}
    (0, X()) in d.items()
