# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_bad_switch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.run_main(switches=['--bad-switch'])
    self.assertEqual(s, dedent('            option --bad-switch not recognized\n            use -h/--help for command line help\n            '))
