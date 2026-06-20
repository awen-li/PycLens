# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CoverageOneHundredTestCase_test_interpolation_validation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = configparser.ConfigParser()
    parser.read_string('\n            [section]\n            invalid_percent = %\n            invalid_reference = %(()\n            invalid_variable = %(does_not_exist)s\n        ')
    with self.assertRaises(configparser.InterpolationSyntaxError) as cm:
        parser['section']['invalid_percent']
    self.assertEqual(str(cm.exception), "'%' must be followed by '%' or '(', found: '%'")
    with self.assertRaises(configparser.InterpolationSyntaxError) as cm:
        parser['section']['invalid_reference']
    self.assertEqual(str(cm.exception), "bad interpolation variable reference '%(()'")
