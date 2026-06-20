# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCoverage_test_coverageresults_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    infile = TESTFN + '-infile'
    with open(infile, 'wb') as f:
        dump(({}, {}, {'caller': 1}), f, protocol=1)
    self.addCleanup(unlink, infile)
    results = trace.CoverageResults({}, {}, infile, {})
    self.assertEqual(results.callers, {'caller': 1})
