# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_finalization_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import os\n            import threading\n            import time\n            import random\n\n            def random_sleep():\n                seconds = random.random() * 0.010\n                time.sleep(seconds)\n\n            class Sleeper:\n                def __del__(self):\n                    random_sleep()\n\n            tls = threading.local()\n\n            def f():\n                # Sleep a bit so that the thread is still running when\n                # Py_Finalize() is called.\n                random_sleep()\n                tls.x = Sleeper()\n                random_sleep()\n\n            threading.Thread(target=f).start()\n            random_sleep()\n        '
    (rc, out, err) = assert_python_ok('-c', code)
    self.assertEqual(err, b'')
