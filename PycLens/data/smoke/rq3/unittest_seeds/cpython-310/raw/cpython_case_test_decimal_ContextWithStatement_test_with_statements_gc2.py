# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextWithStatement_test_with_statements_gc2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    localcontext = self.decimal.localcontext
    with localcontext() as c1:
        with localcontext(c1) as c2:
            del c1
            with localcontext(c2) as c3:
                del c2
                with localcontext(c3) as c4:
                    del c3
                    del c4
