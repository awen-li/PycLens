# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_except_stopiter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def woohoo():
        yield

    class StopIterationSubclass(StopIteration):
        pass
    for stop_exc in (StopIteration('spam'), StopIterationSubclass('spam')):
        with self.subTest(type=type(stop_exc)):
            try:
                with woohoo():
                    raise stop_exc
            except Exception as ex:
                self.assertIs(ex, stop_exc)
            else:
                self.fail(f'{stop_exc} was suppressed')
