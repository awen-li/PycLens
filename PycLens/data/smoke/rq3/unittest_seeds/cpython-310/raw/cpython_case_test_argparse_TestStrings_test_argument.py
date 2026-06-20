# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestStrings_test_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    argument = argparse.Action(option_strings=[], dest='x', type=float, nargs='?', default=2.5, choices=[0.5, 1.5, 2.5], required=True, help='H HH H', metavar='MV MV MV')
    string = "Action(option_strings=[], dest='x', nargs='?', const=None, default=2.5, type=%r, choices=[0.5, 1.5, 2.5], required=True, help='H HH H', metavar='MV MV MV')" % float
    self.assertStringEqual(argument, string)
