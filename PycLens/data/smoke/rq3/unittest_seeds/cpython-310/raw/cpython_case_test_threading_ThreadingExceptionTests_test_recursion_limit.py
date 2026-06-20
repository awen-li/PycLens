# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadingExceptionTests_test_recursion_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = "if True:\n            import threading\n\n            def recurse():\n                return recurse()\n\n            def outer():\n                try:\n                    recurse()\n                except RecursionError:\n                    pass\n\n            w = threading.Thread(target=outer)\n            w.start()\n            w.join()\n            print('end of main thread')\n            "
    expected_output = 'end of main thread\n'
    p = subprocess.Popen([sys.executable, '-c', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    data = stdout.decode().replace('\r', '')
    self.assertEqual(p.returncode, 0, 'Unexpected error: ' + stderr.decode())
    self.assertEqual(data, expected_output)
