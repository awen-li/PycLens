# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseExtendedInterpolation_test_case_sensitivity_conflicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ini = textwrap.dedent('\n            [common]\n            option = value\n            Option = Value\n\n            [Common]\n            option = a better ${common:option}\n            Option = A Better ${common:Option}\n\n            [random]\n            foo = ${common:option} redefined\n            Foo = ${Common:Option} Redefined\n        ').strip()
    with self.assertRaises(configparser.DuplicateOptionError):
        cf = self.fromstring(ini)
    cf = self.fromstring(ini, optionxform=lambda opt: opt)
    eq = self.assertEqual
    eq(cf['common']['option'], 'value')
    eq(cf['common']['Option'], 'Value')
    eq(cf['Common']['option'], 'a better value')
    eq(cf['Common']['Option'], 'A Better Value')
    eq(cf['random']['foo'], 'value redefined')
    eq(cf['random']['Foo'], 'A Better Value Redefined')
