# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: FindmatchTest_test_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    caps = {'test/pass': [{'test': 'test 1 -eq 1'}], 'test/fail': [{'test': 'test 1 -eq 0'}]}
    cases = [([caps, 'test/pass', 'test'], {}, ('test 1 -eq 1', {'test': 'test 1 -eq 1'})), ([caps, 'test/fail', 'test'], {}, (None, None))]
    self._run_cases(cases)
