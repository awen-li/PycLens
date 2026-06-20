# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_telnetlib.py
# case: OptionTests_test_IAC_commands

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cmd in self.cmds:
        self._test_command([tl.IAC, cmd])
        self._test_command([b'x' * 100, tl.IAC, cmd, b'y' * 100])
        self._test_command([b'x' * 10, tl.IAC, cmd, b'y' * 10])
    self._test_command([tl.IAC + cmd for cmd in self.cmds])
