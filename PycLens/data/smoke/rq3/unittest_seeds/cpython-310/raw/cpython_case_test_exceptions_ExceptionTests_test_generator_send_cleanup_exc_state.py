# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_generator_send_cleanup_exc_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def do_send(g):
        try:
            g.send(None)
        except StopIteration:
            pass
        else:
            self.fail('should have raised StopIteration')
    self._check_generator_cleanup_exc_state(do_send)
