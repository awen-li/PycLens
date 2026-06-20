# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = {'names with spaces': 'should be presented using repr()', 'others.should.not.be': 'like.this'}
    exp = "{'names with spaces': 'should be presented using repr()',\n others.should.not.be: like.this}"
    dotted_printer = DottedPrettyPrinter()
    self.assertEqual(dotted_printer.pformat(o), exp)
    o1 = ['with space']
    exp1 = "['with space']"
    self.assertEqual(dotted_printer.pformat(o1), exp1)
    o2 = ['without.space']
    exp2 = '[without.space]'
    self.assertEqual(dotted_printer.pformat(o2), exp2)
