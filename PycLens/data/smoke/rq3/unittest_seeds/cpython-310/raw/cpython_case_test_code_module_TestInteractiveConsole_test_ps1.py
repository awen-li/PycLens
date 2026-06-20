# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_ps1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = EOFError('Finished')
    self.console.interact()
    self.assertEqual(self.sysmod.ps1, '>>> ')
    self.sysmod.ps1 = 'custom1> '
    self.console.interact()
    self.assertEqual(self.sysmod.ps1, 'custom1> ')
