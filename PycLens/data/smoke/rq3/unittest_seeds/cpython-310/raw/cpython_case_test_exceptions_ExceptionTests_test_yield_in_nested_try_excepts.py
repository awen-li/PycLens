# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_yield_in_nested_try_excepts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MainError(Exception):
        pass

    class SubError(Exception):
        pass

    def main():
        try:
            raise MainError()
        except MainError:
            try:
                yield
            except SubError:
                pass
            raise
    coro = main()
    coro.send(None)
    with self.assertRaises(MainError):
        coro.throw(SubError())
