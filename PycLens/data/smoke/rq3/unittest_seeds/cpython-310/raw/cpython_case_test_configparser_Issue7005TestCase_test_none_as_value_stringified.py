# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: Issue7005TestCase_test_none_as_value_stringified

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cp = configparser.ConfigParser(allow_no_value=False)
    cp.add_section('section')
    with self.assertRaises(TypeError):
        cp.set('section', 'option', None)
