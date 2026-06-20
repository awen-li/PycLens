# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_ignored_deprecations_are_silent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings(record=True) as warning_objs:
        warnings_helper._warn_about_deprecation()
        warnings.warn('You should NOT be seeing this.', DeprecationWarning)
        messages = [str(w.message) for w in warning_objs]
    self.assertEqual(len(messages), 0, messages)
