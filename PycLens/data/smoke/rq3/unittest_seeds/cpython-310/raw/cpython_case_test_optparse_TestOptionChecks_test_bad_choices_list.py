# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_bad_choices_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    typename = type('').__name__
    self.assertOptionError("option -b/--bad: choices must be a list of strings ('%s' supplied)" % typename, ['-b', '--bad'], {'type': 'choice', 'choices': 'bad choices'})
