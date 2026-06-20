# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_dont_reraise_RuntimeError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UniqueException(Exception):
        pass

    class UniqueRuntimeError(RuntimeError):
        pass

    @contextmanager
    def second():
        try:
            yield 1
        except Exception as exc:
            raise UniqueException('new exception') from exc

    @contextmanager
    def first():
        try:
            yield 1
        except Exception as exc:
            raise exc
    with self.assertRaises(UniqueException) as err_ctx:
        with self.exit_stack() as es_ctx:
            es_ctx.enter_context(second())
            es_ctx.enter_context(first())
            raise UniqueRuntimeError('please no infinite loop.')
    exc = err_ctx.exception
    self.assertIsInstance(exc, UniqueException)
    self.assertIsInstance(exc.__context__, UniqueRuntimeError)
    self.assertIsNone(exc.__context__.__context__)
    self.assertIsNone(exc.__context__.__cause__)
    self.assertIs(exc.__cause__, exc.__context__)
