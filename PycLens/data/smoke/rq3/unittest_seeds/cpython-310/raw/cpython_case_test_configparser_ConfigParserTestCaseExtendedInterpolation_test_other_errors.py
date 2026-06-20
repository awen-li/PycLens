# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseExtendedInterpolation_test_other_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring("\n            [interpolation fail]\n            case1 = ${where's the brace\n            case2 = ${does_not_exist}\n            case3 = ${wrong_section:wrong_value}\n            case4 = ${i:like:colon:characters}\n            case5 = $100 for Fail No 5!\n        ")
    with self.assertRaises(configparser.InterpolationSyntaxError):
        cf['interpolation fail']['case1']
    with self.assertRaises(configparser.InterpolationMissingOptionError):
        cf['interpolation fail']['case2']
    with self.assertRaises(configparser.InterpolationMissingOptionError):
        cf['interpolation fail']['case3']
    with self.assertRaises(configparser.InterpolationSyntaxError):
        cf['interpolation fail']['case4']
    with self.assertRaises(configparser.InterpolationSyntaxError):
        cf['interpolation fail']['case5']
    with self.assertRaises(ValueError):
        cf['interpolation fail']['case6'] = 'BLACK $ABBATH'
