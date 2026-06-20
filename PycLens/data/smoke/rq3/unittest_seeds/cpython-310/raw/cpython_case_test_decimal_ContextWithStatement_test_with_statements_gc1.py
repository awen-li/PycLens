# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextWithStatement_test_with_statements_gc1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    localcontext = self.decimal.localcontext
    with localcontext() as c1:
        del c1
        with localcontext() as c2:
            del c2
            with localcontext() as c3:
                del c3
                with localcontext() as c4:
                    del c4
