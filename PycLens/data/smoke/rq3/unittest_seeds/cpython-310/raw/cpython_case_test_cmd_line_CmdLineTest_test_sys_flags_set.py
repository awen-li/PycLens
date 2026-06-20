# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_sys_flags_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (value, expected) in (('', 0), ('1', 1), ('text', 1), ('2', 2)):
        env_vars = dict(PYTHONDEBUG=value, PYTHONOPTIMIZE=value, PYTHONDONTWRITEBYTECODE=value, PYTHONVERBOSE=value)
        dont_write_bytecode = int(bool(value))
        code = f'import sys; sys.stderr.write(str(sys.flags)); sys.exit(not (\n                    sys.flags.debug == sys.flags.optimize ==\n                    sys.flags.verbose ==\n                    {expected}\n                    and sys.flags.dont_write_bytecode == {dont_write_bytecode}\n                ))'
        with self.subTest(envar_value=value):
            assert_python_ok('-c', code, **env_vars)
