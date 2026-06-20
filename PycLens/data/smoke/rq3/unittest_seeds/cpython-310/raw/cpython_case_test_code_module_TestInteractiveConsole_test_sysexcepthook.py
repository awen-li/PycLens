# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_sysexcepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = ["raise ValueError('')", EOFError('Finished')]
    hook = mock.Mock()
    self.sysmod.excepthook = hook
    self.console.interact()
    self.assertTrue(hook.called)
