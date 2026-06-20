# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_function_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('\nmodule os\nos.stat as os_stat_fn\n\n   path: str\n       Path to be examined\n\nPerform a stat system call on the given path.')
    self.assertEqual('\nstat($module, /, path)\n--\n\nPerform a stat system call on the given path.\n\n  path\n    Path to be examined\n'.strip(), function.docstring)
