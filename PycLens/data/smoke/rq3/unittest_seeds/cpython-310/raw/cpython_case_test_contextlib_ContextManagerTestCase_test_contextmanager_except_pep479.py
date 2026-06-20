# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_except_pep479

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'from __future__ import generator_stop\nfrom contextlib import contextmanager\n@contextmanager\ndef woohoo():\n    yield\n'
    locals = {}
    exec(code, locals, locals)
    woohoo = locals['woohoo']
    stop_exc = StopIteration('spam')
    try:
        with woohoo():
            raise stop_exc
    except Exception as ex:
        self.assertIs(ex, stop_exc)
    else:
        self.fail('StopIteration was suppressed')
