# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_attr_syntax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = [('starttag', 'a', [('b', 'v'), ('c', 'v'), ('d', 'v'), ('e', None)])]
    self._run_check('<a b=\'v\' c="v" d=v e>', output)
    self._run_check('<a  b = \'v\' c = "v" d = v e>', output)
    self._run_check('<a\nb\n=\n\'v\'\nc\n=\n"v"\nd\n=\nv\ne>', output)
    self._run_check('<a\tb\t=\t\'v\'\tc\t=\t"v"\td\t=\tv\te>', output)
