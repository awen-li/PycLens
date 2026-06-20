# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseExtendedInterpolation_test_case_sensitivity_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ini = textwrap.dedent('\n            [common]\n            optionlower = value\n            OptionUpper = Value\n\n            [Common]\n            optionlower = a better ${common:optionlower}\n            OptionUpper = A Better ${common:OptionUpper}\n\n            [random]\n            foolower = ${common:optionlower} redefined\n            FooUpper = ${Common:OptionUpper} Redefined\n        ').strip()
    cf = self.fromstring(ini)
    eq = self.assertEqual
    eq(cf['common']['optionlower'], 'value')
    eq(cf['common']['OptionUpper'], 'Value')
    eq(cf['Common']['optionlower'], 'a better value')
    eq(cf['Common']['OptionUpper'], 'A Better Value')
    eq(cf['random']['foolower'], 'value redefined')
    eq(cf['random']['FooUpper'], 'A Better Value Redefined')
