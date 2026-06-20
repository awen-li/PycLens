# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_exit_msg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = EOFError('Finished')
    self.console.interact(banner='')
    self.assertEqual(len(self.stderr.method_calls), 2)
    err_msg = self.stderr.method_calls[1]
    expected = 'now exiting InteractiveConsole...\n'
    self.assertEqual(err_msg, ['write', (expected,), {}])
    self.stderr.reset_mock()
    self.infunc.side_effect = EOFError('Finished')
    self.console.interact(banner='', exitmsg='')
    self.assertEqual(len(self.stderr.method_calls), 1)
    self.stderr.reset_mock()
    message = 'bye! ζж'
    self.infunc.side_effect = EOFError('Finished')
    self.console.interact(banner='', exitmsg=message)
    self.assertEqual(len(self.stderr.method_calls), 2)
    err_msg = self.stderr.method_calls[1]
    expected = message + '\n'
    self.assertEqual(err_msg, ['write', (expected,), {}])
