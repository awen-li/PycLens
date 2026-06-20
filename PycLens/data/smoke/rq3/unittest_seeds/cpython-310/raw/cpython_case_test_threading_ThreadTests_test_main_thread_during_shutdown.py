# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_main_thread_during_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import gc, threading\n\n            main_thread = threading.current_thread()\n            assert main_thread is threading.main_thread()  # sanity check\n\n            class RefCycle:\n                def __init__(self):\n                    self.cycle = self\n\n                def __del__(self):\n                    print("GC:",\n                          threading.current_thread() is main_thread,\n                          threading.main_thread() is main_thread,\n                          threading.enumerate() == [main_thread])\n\n            RefCycle()\n            gc.collect()  # sanity check\n            x = RefCycle()\n        '
    (_, out, err) = assert_python_ok('-c', code)
    data = out.decode()
    self.assertEqual(err, b'')
    self.assertEqual(data.splitlines(), ['GC: True True True'] * 2)
