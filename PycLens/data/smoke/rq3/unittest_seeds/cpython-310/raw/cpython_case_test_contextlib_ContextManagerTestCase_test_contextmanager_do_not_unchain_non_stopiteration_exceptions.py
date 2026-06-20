# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_do_not_unchain_non_stopiteration_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def test_issue29692():
        try:
            yield
        except Exception as exc:
            raise RuntimeError('issue29692:Chained') from exc
    try:
        with test_issue29692():
            raise ZeroDivisionError
    except Exception as ex:
        self.assertIs(type(ex), RuntimeError)
        self.assertEqual(ex.args[0], 'issue29692:Chained')
        self.assertIsInstance(ex.__cause__, ZeroDivisionError)
    try:
        with test_issue29692():
            raise StopIteration('issue29692:Unchained')
    except Exception as ex:
        self.assertIs(type(ex), StopIteration)
        self.assertEqual(ex.args[0], 'issue29692:Unchained')
        self.assertIsNone(ex.__cause__)
