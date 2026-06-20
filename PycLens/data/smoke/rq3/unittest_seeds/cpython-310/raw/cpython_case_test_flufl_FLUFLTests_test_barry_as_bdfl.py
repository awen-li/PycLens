# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_flufl.py
# case: FLUFLTests_test_barry_as_bdfl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'from __future__ import barry_as_FLUFL\n2 {0} 3'
    compile(code.format('<>'), '<BDFL test>', 'exec', __future__.CO_FUTURE_BARRY_AS_BDFL)
    with self.assertRaises(SyntaxError) as cm:
        compile(code.format('!='), '<FLUFL test>', 'exec', __future__.CO_FUTURE_BARRY_AS_BDFL)
    self.assertRegex(str(cm.exception), "with Barry as BDFL, use '<>' instead of '!='")
    self.assertIn('2 != 3', cm.exception.text)
    self.assertEqual(cm.exception.filename, '<FLUFL test>')
    self.assertEqual(cm.exception.lineno, 2)
    self.assertEqual(cm.exception.offset, 3)
