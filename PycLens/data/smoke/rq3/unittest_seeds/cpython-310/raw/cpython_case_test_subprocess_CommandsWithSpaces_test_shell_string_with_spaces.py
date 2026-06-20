# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: CommandsWithSpaces_test_shell_string_with_spaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.with_spaces('"%s" "%s" "%s"' % (sys.executable, self.fname, 'ab cd'), shell=1)
