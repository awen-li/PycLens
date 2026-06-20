# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadJoinOnShutdown_test_4_daemon_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = "if True:\n            import os\n            import random\n            import sys\n            import time\n            import threading\n\n            thread_has_run = set()\n\n            def random_io():\n                '''Loop for a while sleeping random tiny amounts and doing some I/O.'''\n                while True:\n                    with open(os.__file__, 'rb') as in_f:\n                        stuff = in_f.read(200)\n                        with open(os.devnull, 'wb') as null_f:\n                            null_f.write(stuff)\n                            time.sleep(random.random() / 1995)\n                    thread_has_run.add(threading.current_thread())\n\n            def main():\n                count = 0\n                for _ in range(40):\n                    new_thread = threading.Thread(target=random_io)\n                    new_thread.daemon = True\n                    new_thread.start()\n                    count += 1\n                while len(thread_has_run) < count:\n                    time.sleep(0.001)\n                # Trigger process shutdown\n                sys.exit(0)\n\n            main()\n            "
    (rc, out, err) = assert_python_ok('-c', script)
    self.assertFalse(err)
