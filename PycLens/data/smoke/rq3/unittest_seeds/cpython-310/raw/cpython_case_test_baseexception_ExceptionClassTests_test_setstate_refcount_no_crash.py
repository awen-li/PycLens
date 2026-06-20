# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_baseexception.py
# case: ExceptionClassTests_test_setstate_refcount_no_crash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import gc
    d = {}

    class HashThisKeyWillClearTheDict(str):

        def __hash__(self) -> int:
            d.clear()
            return super().__hash__()

    class Value(str):
        pass
    exc = Exception()
    d[HashThisKeyWillClearTheDict()] = Value()
    exc.__setstate__(d)
    gc.collect()
