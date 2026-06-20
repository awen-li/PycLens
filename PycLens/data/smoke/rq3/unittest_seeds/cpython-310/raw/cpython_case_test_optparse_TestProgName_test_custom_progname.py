# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestProgName_test_custom_progname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = OptionParser(prog='thingy', version='%prog 0.1', usage='%prog arg arg')
    parser.remove_option('-h')
    parser.remove_option('--version')
    expected_usage = 'Usage: thingy arg arg\n'
    self.assertUsage(parser, expected_usage)
    self.assertVersion(parser, 'thingy 0.1')
    self.assertHelp(parser, expected_usage + '\n')
