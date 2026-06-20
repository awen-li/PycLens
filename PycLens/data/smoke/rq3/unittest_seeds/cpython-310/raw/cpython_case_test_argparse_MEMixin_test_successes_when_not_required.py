# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: MEMixin_test_successes_when_not_required

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parse_args = self.get_parser(required=False).parse_args
    successes = self.successes + self.successes_when_not_required
    for (args_string, expected_ns) in successes:
        actual_ns = parse_args(args_string.split())
        self.assertEqual(actual_ns, expected_ns)
