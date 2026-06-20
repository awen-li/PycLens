# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_finalize_running_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import_module('ctypes')
    (rc, out, err) = assert_python_failure('-c', 'if 1:\n            import ctypes, sys, time, _thread\n\n            # This lock is used as a simple event variable.\n            ready = _thread.allocate_lock()\n            ready.acquire()\n\n            # Module globals are cleared before __del__ is run\n            # So we save the functions in class dict\n            class C:\n                ensure = ctypes.pythonapi.PyGILState_Ensure\n                release = ctypes.pythonapi.PyGILState_Release\n                def __del__(self):\n                    state = self.ensure()\n                    self.release(state)\n\n            def waitingThread():\n                x = C()\n                ready.release()\n                time.sleep(100)\n\n            _thread.start_new_thread(waitingThread, ())\n            ready.acquire()  # Be sure the other thread is waiting.\n            sys.exit(42)\n            ')
    self.assertEqual(rc, 42)
