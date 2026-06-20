# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseExtendedInterpolation_test_strange_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('\n            [dollars]\n            $var = $$value\n            $var2 = ${$var}\n            ${sick} = cannot interpolate me\n\n            [interpolated]\n            $other = ${dollars:$var}\n            $trying = ${dollars:${sick}}\n        ')
    self.assertEqual(cf['dollars']['$var'], '$value')
    self.assertEqual(cf['interpolated']['$other'], '$value')
    self.assertEqual(cf['dollars']['${sick}'], 'cannot interpolate me')
    exception_class = configparser.InterpolationMissingOptionError
    with self.assertRaises(exception_class) as cm:
        cf['interpolated']['$trying']
    self.assertEqual(cm.exception.reference, 'dollars:${sick')
    self.assertEqual(cm.exception.args[2], '${dollars:${sick}}')
