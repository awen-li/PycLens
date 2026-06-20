# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadingExceptionTests_test_bare_raise_in_brand_new_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def bare_raise():
        raise

    class Issue27558(threading.Thread):
        exc = None

        def run(self):
            try:
                bare_raise()
            except Exception as exc:
                self.exc = exc
    thread = Issue27558()
    thread.start()
    thread.join()
    self.assertIsNotNone(thread.exc)
    self.assertIsInstance(thread.exc, RuntimeError)
    thread.exc = None
