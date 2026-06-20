# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: DestroyTests_test_still_running

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    interp = interpreters.create()
    with _running(interp):
        self.assertTrue(interpreters.is_running(interp), msg=f'Interp {interp} should be running before destruction.')
        with self.assertRaises(RuntimeError, msg=f"Should not be able to destroy interp {interp} while it's still running."):
            interpreters.destroy(interp)
        self.assertTrue(interpreters.is_running(interp))
