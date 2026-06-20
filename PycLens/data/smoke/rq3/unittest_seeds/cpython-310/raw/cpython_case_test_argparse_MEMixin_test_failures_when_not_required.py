# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: MEMixin_test_failures_when_not_required

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parse_args = self.get_parser(required=False).parse_args
    error = ArgumentParserError
    for args_string in self.failures:
        self.assertRaises(error, parse_args, args_string.split())
