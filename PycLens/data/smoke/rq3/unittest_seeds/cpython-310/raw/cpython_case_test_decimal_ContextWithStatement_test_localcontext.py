# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextWithStatement_test_localcontext

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    getcontext = self.decimal.getcontext
    localcontext = self.decimal.localcontext
    orig_ctx = getcontext()
    with localcontext() as enter_ctx:
        set_ctx = getcontext()
    final_ctx = getcontext()
    self.assertIs(orig_ctx, final_ctx, 'did not restore context correctly')
    self.assertIsNot(orig_ctx, set_ctx, 'did not copy the context')
    self.assertIs(set_ctx, enter_ctx, '__enter__ returned wrong context')
