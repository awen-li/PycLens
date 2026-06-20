# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_comparison_equivalent_exceptions_are_equal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    excs = []
    for _ in range(2):
        try:
            1 / 0
        except:
            excs.append(traceback.TracebackException(*sys.exc_info()))
    self.assertEqual(excs[0], excs[1])
    self.assertEqual(list(excs[0].format()), list(excs[1].format()))
