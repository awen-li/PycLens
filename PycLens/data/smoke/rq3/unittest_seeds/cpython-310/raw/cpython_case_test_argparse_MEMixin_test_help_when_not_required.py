# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: MEMixin_test_help_when_not_required

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    format_help = self.get_parser(required=False).format_help
    help = self.usage_when_not_required + self.help
    self.assertEqual(format_help(), textwrap.dedent(help))
