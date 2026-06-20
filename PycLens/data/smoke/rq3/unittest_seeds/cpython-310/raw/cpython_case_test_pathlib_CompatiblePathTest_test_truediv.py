# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: CompatiblePathTest_test_truediv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = pathlib.PurePath('test') / self.CompatPath('right')
    self.assertIsInstance(result, self.CompatPath)
    self.assertEqual(result.string, 'test/right')
    with self.assertRaises(TypeError):
        pathlib.PurePath('test') / 10
