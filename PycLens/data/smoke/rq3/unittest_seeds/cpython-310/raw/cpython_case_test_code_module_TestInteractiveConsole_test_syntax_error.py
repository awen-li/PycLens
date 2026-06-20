# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_syntax_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = ['undefined', EOFError('Finished')]
    self.console.interact()
    for call in self.stderr.method_calls:
        if 'NameError' in ''.join(call[1]):
            break
    else:
        raise AssertionError('No syntax error from console')
