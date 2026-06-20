# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_do_not_unchain_non_stopiteration_exceptions_test_issue29692

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        yield
    except Exception as exc:
        raise RuntimeError('issue29692:Chained') from exc
