# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_not_last

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = Exception('context')
    try:
        raise context
    except Exception:
        try:
            raise Exception('caught')
        except Exception:
            pass
        try:
            raise Exception('new')
        except Exception as exc:
            raised = exc
    self.assertIs(raised.__context__, context)
