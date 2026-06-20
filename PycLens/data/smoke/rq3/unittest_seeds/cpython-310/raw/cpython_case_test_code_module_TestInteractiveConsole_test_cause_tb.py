# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code_module.py
# case: TestInteractiveConsole_test_cause_tb

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.infunc.side_effect = ["raise ValueError('') from AttributeError", EOFError('Finished')]
    self.console.interact()
    output = ''.join((''.join(call[1]) for call in self.stderr.method_calls))
    expected = dedent('\n        AttributeError\n\n        The above exception was the direct cause of the following exception:\n\n        Traceback (most recent call last):\n          File "<console>", line 1, in <module>\n        ValueError\n        ')
    self.assertIn(expected, output)
