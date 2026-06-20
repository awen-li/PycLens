# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_context_tb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = ['try: ham\nexcept: eggs\n', EOFError('Finished')]
    self.console.interact()
    output = ''.join((''.join(call[1]) for call in self.stderr.method_calls))
    expected = dedent('\n        Traceback (most recent call last):\n          File "<console>", line 1, in <module>\n        NameError: name \'ham\' is not defined\n\n        During handling of the above exception, another exception occurred:\n\n        Traceback (most recent call last):\n          File "<console>", line 2, in <module>\n        NameError: name \'eggs\' is not defined\n        ')
    self.assertIn(expected, output)
