# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_banner

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = EOFError('Finished')
    self.console.interact(banner='Foo')
    self.assertEqual(len(self.stderr.method_calls), 3)
    banner_call = self.stderr.method_calls[0]
    self.assertEqual(banner_call, ['write', ('Foo\n',), {}])
    self.stderr.reset_mock()
    self.infunc.side_effect = EOFError('Finished')
    self.console.interact(banner='')
    self.assertEqual(len(self.stderr.method_calls), 2)
