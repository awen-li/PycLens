# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_global_matches

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(sorted(self.stdcompleter.global_matches('di')), [x + '(' for x in dir(builtins) if x.startswith('di')])
    self.assertEqual(sorted(self.stdcompleter.global_matches('st')), [x + '(' for x in dir(builtins) if x.startswith('st')])
    self.assertEqual(self.stdcompleter.global_matches('akaksajadhak'), [])
    self.assertEqual(self.completer.global_matches('CompleteM'), ['CompleteMe()'])
    self.assertEqual(self.completer.global_matches('eg'), ['egg('])
    self.assertEqual(self.completer.global_matches('CompleteM'), ['CompleteMe()'])
