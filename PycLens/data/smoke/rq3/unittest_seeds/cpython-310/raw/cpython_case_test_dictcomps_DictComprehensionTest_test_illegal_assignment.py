# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictcomps.py
# case: DictComprehensionTest_test_illegal_assignment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(SyntaxError, 'cannot assign'):
        compile('{x: y for y, x in ((1, 2), (3, 4))} = 5', '<test>', 'exec')
    with self.assertRaisesRegex(SyntaxError, 'illegal expression'):
        compile('{x: y for y, x in ((1, 2), (3, 4))} += 5', '<test>', 'exec')
