# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: CompatiblePathTest_test_rtruediv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.CompatPath('left') / pathlib.PurePath('test')
    self.assertIsInstance(result, self.CompatPath)
    self.assertEqual(result.string, 'left/test')
    with self.assertRaises(TypeError):
        10 / pathlib.PurePath('test')
