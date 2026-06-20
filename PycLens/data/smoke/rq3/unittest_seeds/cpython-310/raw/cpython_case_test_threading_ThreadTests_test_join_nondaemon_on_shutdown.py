# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_join_nondaemon_on_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'if 1:\n                import threading\n                from time import sleep\n\n                def child():\n                    sleep(1)\n                    # As a non-daemon thread we SHOULD wake up and nothing\n                    # should be torn down yet\n                    print("Woke up, sleep function is:", sleep)\n\n                threading.Thread(target=child).start()\n                raise SystemExit\n            ')
    self.assertEqual(out.strip(), b'Woke up, sleep function is: <built-in function sleep>')
    self.assertEqual(err, b'')
