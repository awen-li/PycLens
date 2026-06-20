# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_xdev

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; print(sys.flags.dev_mode)'
    out = self.run_xdev('-c', code, xdev=False)
    self.assertEqual(out, 'False')
    out = self.run_xdev('-c', code)
    self.assertEqual(out, 'True')
    code = "import warnings; print(' '.join('%s::%s' % (f[0], f[2].__name__) for f in warnings.filters))"
    if Py_DEBUG:
        expected_filters = 'default::Warning'
    else:
        expected_filters = 'default::Warning default::DeprecationWarning ignore::DeprecationWarning ignore::PendingDeprecationWarning ignore::ImportWarning ignore::ResourceWarning'
    out = self.run_xdev('-c', code)
    self.assertEqual(out, expected_filters)
    out = self.run_xdev('-b', '-c', code)
    self.assertEqual(out, f'default::BytesWarning {expected_filters}')
    out = self.run_xdev('-bb', '-c', code)
    self.assertEqual(out, f'error::BytesWarning {expected_filters}')
    out = self.run_xdev('-Werror', '-c', code)
    self.assertEqual(out, f'error::Warning {expected_filters}')
    try:
        import _testcapi
    except ImportError:
        pass
    else:
        code = 'import _testcapi; print(_testcapi.pymem_getallocatorsname())'
        with support.SuppressCrashReport():
            out = self.run_xdev('-c', code, check_exitcode=False)
        if support.with_pymalloc():
            alloc_name = 'pymalloc_debug'
        else:
            alloc_name = 'malloc_debug'
        self.assertEqual(out, alloc_name)
    try:
        import faulthandler
    except ImportError:
        pass
    else:
        code = 'import faulthandler; print(faulthandler.is_enabled())'
        out = self.run_xdev('-c', code)
        self.assertEqual(out, 'True')
