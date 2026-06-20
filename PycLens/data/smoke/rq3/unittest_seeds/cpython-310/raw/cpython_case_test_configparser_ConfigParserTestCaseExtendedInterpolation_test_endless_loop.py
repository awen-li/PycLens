# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseExtendedInterpolation_test_endless_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring(textwrap.dedent('\n            [one for you]\n            ping = ${one for me:pong}\n\n            [one for me]\n            pong = ${one for you:ping}\n\n            [selfish]\n            me = ${me}\n        ').strip())
    with self.assertRaises(configparser.InterpolationDepthError):
        cf['one for you']['ping']
    with self.assertRaises(configparser.InterpolationDepthError):
        cf['selfish']['me']
