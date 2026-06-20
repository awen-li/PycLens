# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_main_thread_after_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import os, threading\n            from test import support\n\n            pid = os.fork()\n            if pid == 0:\n                main = threading.main_thread()\n                print(main.name)\n                print(main.ident == threading.current_thread().ident)\n                print(main.ident == threading.get_ident())\n            else:\n                support.wait_process(pid, exitcode=0)\n        '
    (_, out, err) = assert_python_ok('-c', code)
    data = out.decode().replace('\r', '')
    self.assertEqual(err, b'')
    self.assertEqual(data, 'MainThread\nTrue\nTrue\n')
