# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_garbage_at_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import subprocess
    code = 'if 1:\n            import gc\n            import _testcapi\n            @_testcapi.with_tp_del\n            class X:\n                def __init__(self, name):\n                    self.name = name\n                def __repr__(self):\n                    return "<X %%r>" %% self.name\n                def __tp_del__(self):\n                    pass\n\n            x = X(\'first\')\n            x.x = x\n            x.y = X(\'second\')\n            del x\n            gc.set_debug(%s)\n        '

    def run_command(code):
        p = subprocess.Popen([sys.executable, '-Wd', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = p.communicate()
        p.stdout.close()
        p.stderr.close()
        self.assertEqual(p.returncode, 0)
        self.assertEqual(stdout, b'')
        return stderr
    stderr = run_command(code % '0')
    self.assertIn(b'ResourceWarning: gc: 2 uncollectable objects at shutdown; use', stderr)
    self.assertNotIn(b"<X 'first'>", stderr)
    stderr = run_command(code % 'gc.DEBUG_UNCOLLECTABLE')
    self.assertIn(b'ResourceWarning: gc: 2 uncollectable objects at shutdown', stderr)
    self.assertTrue(b"[<X 'first'>, <X 'second'>]" in stderr or b"[<X 'second'>, <X 'first'>]" in stderr, stderr)
    stderr = run_command(code % 'gc.DEBUG_SAVEALL')
    self.assertNotIn(b'uncollectable objects at shutdown', stderr)
