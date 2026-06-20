# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_locals_at_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'if 1:\n            import threading\n\n            class Atexit:\n                def __del__(self):\n                    print("thread_dict.atexit = %r" % thread_dict.atexit)\n\n            thread_dict = threading.local()\n            thread_dict.atexit = "value"\n\n            atexit = Atexit()\n        ')
    self.assertEqual(out.rstrip(), b"thread_dict.atexit = 'value'")
