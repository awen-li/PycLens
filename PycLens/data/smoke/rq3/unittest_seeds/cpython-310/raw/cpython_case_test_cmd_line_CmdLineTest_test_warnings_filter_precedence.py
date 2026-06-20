# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_warnings_filter_precedence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_filters = 'error::BytesWarning once::UserWarning always::UserWarning'
    if not Py_DEBUG:
        expected_filters += ' default::DeprecationWarning ignore::DeprecationWarning ignore::PendingDeprecationWarning ignore::ImportWarning ignore::ResourceWarning'
    out = self.check_warnings_filters('once::UserWarning', 'always::UserWarning')
    self.assertEqual(out, expected_filters)
    out = self.check_warnings_filters('once::UserWarning', 'always::UserWarning', use_pywarning=True)
    self.assertEqual(out, expected_filters)
