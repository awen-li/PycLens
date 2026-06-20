# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_namedtuple_field_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Box = namedtuple('Box', ('width', 'height'))
    self.assertEqual(self._get_summary_lines(Box.width), '    Alias for field number 0\n')
