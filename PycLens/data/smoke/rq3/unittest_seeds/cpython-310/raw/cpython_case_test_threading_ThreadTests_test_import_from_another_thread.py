# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_import_from_another_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent("\n            import _thread\n            import sys\n\n            event = _thread.allocate_lock()\n            event.acquire()\n\n            def import_threading():\n                import threading\n                event.release()\n\n            if 'threading' in sys.modules:\n                raise Exception('threading is already imported')\n\n            _thread.start_new_thread(import_threading, ())\n\n            # wait until the threading module is imported\n            event.acquire()\n            event.release()\n\n            if 'threading' not in sys.modules:\n                raise Exception('threading is not imported')\n\n            # don't wait until the thread completes\n        ")
    (rc, out, err) = assert_python_ok('-c', code)
    self.assertEqual(out, b'')
    self.assertEqual(err, b'')
