# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestStrings_test_parser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = argparse.ArgumentParser(prog='PROG')
    string = "ArgumentParser(prog='PROG', usage=None, description=None, formatter_class=%r, conflict_handler='error', add_help=True)" % argparse.HelpFormatter
    self.assertStringEqual(parser, string)
