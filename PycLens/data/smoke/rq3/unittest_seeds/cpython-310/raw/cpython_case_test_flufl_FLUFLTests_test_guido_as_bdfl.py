# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_flufl.py
# case: FLUFLTests_test_guido_as_bdfl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '2 {0} 3'
    compile(code.format('!='), '<BDFL test>', 'exec')
    with self.assertRaises(SyntaxError) as cm:
        compile(code.format('<>'), '<FLUFL test>', 'exec')
    self.assertRegex(str(cm.exception), 'invalid syntax')
    self.assertIn('2 <> 3', cm.exception.text)
    self.assertEqual(cm.exception.filename, '<FLUFL test>')
    self.assertEqual(cm.exception.lineno, 1)
    self.assertEqual(cm.exception.offset, 3)
