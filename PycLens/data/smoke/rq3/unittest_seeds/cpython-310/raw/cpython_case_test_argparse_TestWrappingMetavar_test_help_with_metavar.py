# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestWrappingMetavar_test_help_with_metavar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    help_text = self.parser.format_help()
    self.assertEqual(help_text, textwrap.dedent('            usage: this_is_spammy_prog_with_a_long_name_sorry_about_the_name\n                   [-h] [--proxy <http[s]://example:1234>]\n\n            options:\n              -h, --help            show this help message and exit\n              --proxy <http[s]://example:1234>\n            '))
