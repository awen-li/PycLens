# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_sys_tracebacklimit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import sys\n            def f1():\n                1 / 0\n            def f2():\n                f1()\n            sys.tracebacklimit = %r\n            f2()\n        '

    def check(tracebacklimit, expected):
        p = subprocess.Popen([sys.executable, '-c', code % tracebacklimit], stderr=subprocess.PIPE)
        out = p.communicate()[1]
        self.assertEqual(out.splitlines(), expected)
    traceback = [b'Traceback (most recent call last):', b'  File "<string>", line 8, in <module>', b'  File "<string>", line 6, in f2', b'  File "<string>", line 4, in f1', b'ZeroDivisionError: division by zero']
    check(10, traceback)
    check(3, traceback)
    check(2, traceback[:1] + traceback[2:])
    check(1, traceback[:1] + traceback[3:])
    check(0, [traceback[-1]])
    check(-1, [traceback[-1]])
    check(1 << 1000, traceback)
    check(-1 << 1000, [traceback[-1]])
    check(None, traceback)
