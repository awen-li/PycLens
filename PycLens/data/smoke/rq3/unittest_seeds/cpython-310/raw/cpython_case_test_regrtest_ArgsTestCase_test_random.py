# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_random

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import random\n            print("TESTRANDOM: %s" % random.randint(1, 1000))\n        ')
    test = self.create_test('random', code)
    output = self.run_tests('-r', test)
    randseed = self.parse_random_seed(output)
    match = self.regex_search('TESTRANDOM: ([0-9]+)', output)
    test_random = int(match.group(1))
    output = self.run_tests('-r', '--randseed=%s' % randseed, test)
    randseed2 = self.parse_random_seed(output)
    self.assertEqual(randseed2, randseed)
    match = self.regex_search('TESTRANDOM: ([0-9]+)', output)
    test_random2 = int(match.group(1))
    self.assertEqual(test_random2, test_random)
