# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCCallbackTests_test_refcount_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.preclean()
    import_module('ctypes')
    import subprocess
    code = textwrap.dedent('\n            from test.support import gc_collect, SuppressCrashReport\n\n            a = [1, 2, 3]\n            b = [a]\n\n            # Avoid coredump when Py_FatalError() calls abort()\n            SuppressCrashReport().__enter__()\n\n            # Simulate the refcount of "a" being too low (compared to the\n            # references held on it by live data), but keeping it above zero\n            # (to avoid deallocating it):\n            import ctypes\n            ctypes.pythonapi.Py_DecRef(ctypes.py_object(a))\n\n            # The garbage collector should now have a fatal error\n            # when it reaches the broken object\n            gc_collect()\n        ')
    p = subprocess.Popen([sys.executable, '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    p.stdout.close()
    p.stderr.close()
    self.assertRegex(stderr, b'gcmodule\\.c:[0-9]+: gc_decref: Assertion "gc_get_refs\\(g\\) > 0" failed.')
    self.assertRegex(stderr, b'refcount is too small')
    address_regex = b'[0-9a-fA-Fx]+'
    self.assertRegex(stderr, b'object address  : ' + address_regex)
    self.assertRegex(stderr, b'object refcount : 1')
    self.assertRegex(stderr, b'object type     : ' + address_regex)
    self.assertRegex(stderr, b'object type name: list')
    self.assertRegex(stderr, b'object repr     : \\[1, 2, 3\\]')
