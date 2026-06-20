# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: SubinterpThreadingTests_test_threads_join_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = self.pipe()
    code = textwrap.dedent('\n            import os\n            import random\n            import threading\n            import time\n\n            def random_sleep():\n                seconds = random.random() * 0.010\n                time.sleep(seconds)\n\n            class Sleeper:\n                def __del__(self):\n                    random_sleep()\n\n            tls = threading.local()\n\n            def f():\n                # Sleep a bit so that the thread is still running when\n                # Py_EndInterpreter is called.\n                random_sleep()\n                tls.x = Sleeper()\n                os.write(%d, b"x")\n\n            threading.Thread(target=f).start()\n            random_sleep()\n        ' % (w,))
    ret = test.support.run_in_subinterp(code)
    self.assertEqual(ret, 0)
    self.assertEqual(os.read(r, 1), b'x')
