# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ParseErrorTest_test_error_position

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self._get_error('foo').position, (1, 0))
    self.assertEqual(self._get_error('<tag>&foo;</tag>').position, (1, 5))
    self.assertEqual(self._get_error('foobar<').position, (1, 6))
