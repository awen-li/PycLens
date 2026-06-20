# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseExtendedInterpolation_test_extended_interpolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring(textwrap.dedent('\n            [common]\n            favourite Beatle = Paul\n            favourite color = green\n\n            [tom]\n            favourite band = ${favourite color} day\n            favourite pope = John ${favourite Beatle} II\n            sequel = ${favourite pope}I\n\n            [ambv]\n            favourite Beatle = George\n            son of Edward VII = ${favourite Beatle} V\n            son of George V = ${son of Edward VII}I\n\n            [stanley]\n            favourite Beatle = ${ambv:favourite Beatle}\n            favourite pope = ${tom:favourite pope}\n            favourite color = black\n            favourite state of mind = paranoid\n            favourite movie = soylent ${common:favourite color}\n            favourite song = ${favourite color} sabbath - ${favourite state of mind}\n        ').strip())
    eq = self.assertEqual
    eq(cf['common']['favourite Beatle'], 'Paul')
    eq(cf['common']['favourite color'], 'green')
    eq(cf['tom']['favourite Beatle'], 'Paul')
    eq(cf['tom']['favourite color'], 'green')
    eq(cf['tom']['favourite band'], 'green day')
    eq(cf['tom']['favourite pope'], 'John Paul II')
    eq(cf['tom']['sequel'], 'John Paul III')
    eq(cf['ambv']['favourite Beatle'], 'George')
    eq(cf['ambv']['favourite color'], 'green')
    eq(cf['ambv']['son of Edward VII'], 'George V')
    eq(cf['ambv']['son of George V'], 'George VI')
    eq(cf['stanley']['favourite Beatle'], 'George')
    eq(cf['stanley']['favourite color'], 'black')
    eq(cf['stanley']['favourite state of mind'], 'paranoid')
    eq(cf['stanley']['favourite movie'], 'soylent green')
    eq(cf['stanley']['favourite pope'], 'John Paul II')
    eq(cf['stanley']['favourite song'], 'black sabbath - paranoid')
