# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_no_hang_on_context_chain_cycle1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cycle():
        try:
            raise ValueError(1)
        except ValueError as ex:
            ex.__context__ = ex
            raise TypeError(2)
    try:
        cycle()
    except Exception as e:
        exc = e
    self.assertIsInstance(exc, TypeError)
    self.assertIsInstance(exc.__context__, ValueError)
    self.assertIs(exc.__context__.__context__, exc.__context__)
