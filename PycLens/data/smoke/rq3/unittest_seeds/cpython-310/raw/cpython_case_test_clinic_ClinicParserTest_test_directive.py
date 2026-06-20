# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_directive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = FakeClinic()
    parser = DSLParser(c)
    parser.flag = False
    parser.directives['setflag'] = lambda : setattr(parser, 'flag', True)
    block = clinic.Block('setflag')
    parser.parse(block)
    self.assertTrue(parser.flag)
