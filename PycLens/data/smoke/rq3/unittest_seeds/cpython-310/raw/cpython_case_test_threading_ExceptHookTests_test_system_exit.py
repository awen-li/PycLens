# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ExceptHookTests_test_system_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ThreadExit(threading.Thread):

        def run(self):
            sys.exit(1)
    with support.captured_output('stderr') as stderr:
        thread = ThreadExit()
        thread.start()
        thread.join()
    self.assertEqual(stderr.getvalue(), '')
