# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_console_stderr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = ["'antioch'", '', EOFError('Finished')]
    self.console.interact()
    for call in list(self.stdout.method_calls):
        if 'antioch' in ''.join(call[1]):
            break
    else:
        raise AssertionError('no console stdout')
