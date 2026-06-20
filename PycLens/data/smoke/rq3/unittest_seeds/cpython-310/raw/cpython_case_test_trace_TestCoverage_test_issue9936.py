# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCoverage_test_issue9936

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracer = trace.Trace(trace=0, count=1)
    modname = 'test.tracedmodules.testmod'
    if modname in sys.modules:
        del sys.modules[modname]
    cmd = 'import test.tracedmodules.testmod as t;t.func(0); t.func2();'
    with captured_stdout() as stdout:
        self._coverage(tracer, cmd)
    stdout.seek(0)
    stdout.readline()
    coverage = {}
    for line in stdout:
        (lines, cov, module) = line.split()[:3]
        coverage[module] = (int(lines), int(cov[:-1]))
    modname = trace._fullmodname(sys.modules[modname].__file__)
    self.assertIn(modname, coverage)
    self.assertEqual(coverage[modname], (5, 100))
