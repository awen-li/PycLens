# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCommandLine_test_command_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = findfile('tabnanny.py')
    stderr = f'Usage: {path} [-v] file_or_directory ...'
    self.validate_cmd(stderr=stderr)
