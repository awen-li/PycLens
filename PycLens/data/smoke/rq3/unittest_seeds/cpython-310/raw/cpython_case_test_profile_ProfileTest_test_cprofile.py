# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_profile.py
# case: ProfileTest_test_cprofile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    results = self.do_profiling()
    expected = self.get_expected_output()
    self.assertEqual(results[0], 1000)
    fail = []
    for (i, method) in enumerate(self.methodnames):
        a = expected[method]
        b = results[i + 1]
        if a != b:
            fail.append(f'\nStats.{method} output for {self.profilerclass.__name__} does not fit expectation:')
            fail.extend(unified_diff(a.split('\n'), b.split('\n'), lineterm=''))
    if fail:
        self.fail('\n'.join(fail))
