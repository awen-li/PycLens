# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: MiscTests_test_context_manager_keyboardinterrupt_no_kill

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def popen_via_context_manager(*args, **kwargs):
        with subprocess.Popen(*args, **kwargs) as unused_process:
            raise KeyboardInterrupt
    self._test_keyboardinterrupt_no_kill(popen_via_context_manager)
