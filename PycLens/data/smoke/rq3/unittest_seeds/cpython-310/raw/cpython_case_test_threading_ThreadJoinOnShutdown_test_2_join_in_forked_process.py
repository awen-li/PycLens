# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadJoinOnShutdown_test_2_join_in_forked_process

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = "if 1:\n            from test import support\n\n            childpid = os.fork()\n            if childpid != 0:\n                # parent process\n                support.wait_process(childpid, exitcode=0)\n                sys.exit(0)\n\n            # child process\n            t = threading.Thread(target=joiningfunc,\n                                 args=(threading.current_thread(),))\n            t.start()\n            print('end of main')\n            "
    self._run_and_join(script)
