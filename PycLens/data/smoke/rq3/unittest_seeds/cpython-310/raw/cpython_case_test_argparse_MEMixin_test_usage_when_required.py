# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: MEMixin_test_usage_when_required

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    format_usage = self.get_parser(required=True).format_usage
    expected_usage = self.usage_when_required
    self.assertEqual(format_usage(), textwrap.dedent(expected_usage))
