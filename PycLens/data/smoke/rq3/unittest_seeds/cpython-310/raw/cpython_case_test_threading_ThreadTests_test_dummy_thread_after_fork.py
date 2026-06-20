# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_dummy_thread_after_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import _thread, threading, os, time\n\n            def background_thread(evt):\n                # Creates and registers the _DummyThread instance\n                threading.current_thread()\n                evt.set()\n                time.sleep(10)\n\n            evt = threading.Event()\n            _thread.start_new_thread(background_thread, (evt,))\n            evt.wait()\n            assert threading.active_count() == 2, threading.active_count()\n            if os.fork() == 0:\n                assert threading.active_count() == 1, threading.active_count()\n                os._exit(0)\n            else:\n                os.wait()\n        '
    (_, out, err) = assert_python_ok('-c', code)
    self.assertEqual(out, b'')
    self.assertEqual(err, b'')
