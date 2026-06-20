# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_set_pycache_prefix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NO_VALUE = object()
    cases = [(None, None, None), ('foo', None, 'foo'), (None, 'bar', 'bar'), ('foo', 'bar', 'bar'), ('foo', '', None), ('foo', NO_VALUE, None)]
    for (envval, opt, expected) in cases:
        exp_clause = 'is None' if expected is None else f'== "{expected}"'
        code = f'import sys; sys.exit(not sys.pycache_prefix {exp_clause})'
        args = ['-c', code]
        env = {} if envval is None else {'PYTHONPYCACHEPREFIX': envval}
        if opt is NO_VALUE:
            args[:0] = ['-X', 'pycache_prefix']
        elif opt is not None:
            args[:0] = ['-X', f'pycache_prefix={opt}']
        with self.subTest(envval=envval, opt=opt):
            with os_helper.temp_cwd():
                assert_python_ok(*args, **env)
