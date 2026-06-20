# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_unix_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'You should use the -n option, or --dry-run in its long form.'
    self.check_wrap(text, 20, ['You should use the', '-n option, or --dry-', 'run in its long', 'form.'])
    self.check_wrap(text, 21, ['You should use the -n', 'option, or --dry-run', 'in its long form.'])
    expect = ['You should use the -n option, or', '--dry-run in its long form.']
    self.check_wrap(text, 32, expect)
    self.check_wrap(text, 34, expect)
    self.check_wrap(text, 35, expect)
    self.check_wrap(text, 38, expect)
    expect = ['You should use the -n option, or --dry-', 'run in its long form.']
    self.check_wrap(text, 39, expect)
    self.check_wrap(text, 41, expect)
    expect = ['You should use the -n option, or --dry-run', 'in its long form.']
    self.check_wrap(text, 42, expect)
    text = 'the -n option, or --dry-run or --dryrun'
    expect = ['the', ' ', '-n', ' ', 'option,', ' ', 'or', ' ', '--dry-', 'run', ' ', 'or', ' ', '--dryrun']
    self.check_split(text, expect)
