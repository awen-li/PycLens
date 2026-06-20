# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_getset_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self._get_summary_line(int.numerator), 'numerator')
    self.assertEqual(self._get_summary_line(float.real), 'real')
    self.assertEqual(self._get_summary_line(Exception.args), 'args')
    self.assertEqual(self._get_summary_line(memoryview.obj), 'obj')
