# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestStrings_test_optional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    option = argparse.Action(option_strings=['--foo', '-a', '-b'], dest='b', type='int', nargs='+', default=42, choices=[1, 2, 3], required=False, help='HELP', metavar='METAVAR')
    string = "Action(option_strings=['--foo', '-a', '-b'], dest='b', nargs='+', const=None, default=42, type='int', choices=[1, 2, 3], required=False, help='HELP', metavar='METAVAR')"
    self.assertStringEqual(option, string)
