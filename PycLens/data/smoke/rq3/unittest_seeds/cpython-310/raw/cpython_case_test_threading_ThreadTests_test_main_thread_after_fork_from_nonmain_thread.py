# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_main_thread_after_fork_from_nonmain_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import os, threading, sys\n            from test import support\n\n            def func():\n                pid = os.fork()\n                if pid == 0:\n                    main = threading.main_thread()\n                    print(main.name)\n                    print(main.ident == threading.current_thread().ident)\n                    print(main.ident == threading.get_ident())\n                    # stdout is fully buffered because not a tty,\n                    # we have to flush before exit.\n                    sys.stdout.flush()\n                else:\n                    support.wait_process(pid, exitcode=0)\n\n            th = threading.Thread(target=func)\n            th.start()\n            th.join()\n        '
    (_, out, err) = assert_python_ok('-c', code)
    data = out.decode().replace('\r', '')
    self.assertEqual(err, b'')
    self.assertEqual(data, 'Thread-1 (func)\nTrue\nTrue\n')
