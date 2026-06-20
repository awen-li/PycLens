# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestHelp_test_help_description_groups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.parser.set_description('This is the program description for %prog.  %prog has an option group as well as single options.')
    group = OptionGroup(self.parser, 'Dangerous Options', 'Caution: use of these options is at your own risk.  It is believed that some of them bite.')
    group.add_option('-g', action='store_true', help='Group option.')
    self.parser.add_option_group(group)
    expect = 'Usage: bar.py [options]\n\nThis is the program description for bar.py.  bar.py has an option group as\nwell as single options.\n\nOptions:\n  -a APPLE           throw APPLEs at basket\n  -b NUM, --boo=NUM  shout "boo!" NUM times (in order to frighten away all the\n                     evil spirits that cause trouble and mayhem)\n  --foo=FOO          store FOO in the foo list for later fooing\n  -h, --help         show this help message and exit\n\n  Dangerous Options:\n    Caution: use of these options is at your own risk.  It is believed\n    that some of them bite.\n\n    -g               Group option.\n'
    self.assertHelpEquals(expect)
    self.parser.epilog = 'Please report bugs to /dev/null.'
    self.assertHelpEquals(expect + '\nPlease report bugs to /dev/null.\n')
