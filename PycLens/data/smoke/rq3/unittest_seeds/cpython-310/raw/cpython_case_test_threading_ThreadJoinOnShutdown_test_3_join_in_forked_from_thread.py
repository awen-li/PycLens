# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadJoinOnShutdown_test_3_join_in_forked_from_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = "if 1:\n            from test import support\n\n            main_thread = threading.current_thread()\n            def worker():\n                childpid = os.fork()\n                if childpid != 0:\n                    # parent process\n                    support.wait_process(childpid, exitcode=0)\n                    sys.exit(0)\n\n                # child process\n                t = threading.Thread(target=joiningfunc,\n                                     args=(main_thread,))\n                print('end of main')\n                t.start()\n                t.join() # Should not block: main_thread is already stopped\n\n            w = threading.Thread(target=worker)\n            w.start()\n            "
    self._run_and_join(script)
