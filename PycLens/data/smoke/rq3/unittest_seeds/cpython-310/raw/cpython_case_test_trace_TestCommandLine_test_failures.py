# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCommandLine_test_failures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _errors = ((b'progname is missing: required with the main options', '-l', '-T'), (b'cannot specify both --listfuncs and (--trace or --count)', '-lc'), (b'argument -R/--no-report: not allowed with argument -r/--report', '-rR'), (b'must specify one of --trace, --count, --report, --listfuncs, or --trackcalls', '-g'), (b'-r/--report requires -f/--file', '-r'), (b'--summary can only be used with --count or --report', '-sT'), (b'unrecognized arguments: -y', '-y'))
    for (message, *args) in _errors:
        (*_, stderr) = assert_python_failure('-m', 'trace', *args)
        self.assertIn(message, stderr)
