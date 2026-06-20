# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_finalize_with_trace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert_python_ok('-c', "if 1:\n            import sys, threading\n\n            # A deadlock-killer, to prevent the\n            # testsuite to hang forever\n            def killer():\n                import os, time\n                time.sleep(2)\n                print('program blocked; aborting')\n                os._exit(2)\n            t = threading.Thread(target=killer)\n            t.daemon = True\n            t.start()\n\n            # This is the trace function\n            def func(frame, event, arg):\n                threading.current_thread()\n                return func\n\n            sys.settrace(func)\n            ")
