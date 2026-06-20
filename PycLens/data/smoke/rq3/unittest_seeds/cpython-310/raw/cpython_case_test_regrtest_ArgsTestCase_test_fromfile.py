# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_fromfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [self.create_test() for index in range(5)]
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    with open(filename, 'w') as fp:
        previous = None
        for (index, name) in enumerate(tests, 1):
            line = '00:00:%02i [%s/%s] %s' % (index, index, len(tests), name)
            if previous:
                line += ' -- %s took 0 sec' % previous
            print(line, file=fp)
            previous = name
    output = self.run_tests('--fromfile', filename)
    self.check_executed_tests(output, tests)
    with open(filename, 'w') as fp:
        for (index, name) in enumerate(tests, 1):
            print('[%s/%s] %s' % (index, len(tests), name), file=fp)
    output = self.run_tests('--fromfile', filename)
    self.check_executed_tests(output, tests)
    with open(filename, 'w') as fp:
        for name in tests:
            print(name, file=fp)
    output = self.run_tests('--fromfile', filename)
    self.check_executed_tests(output, tests)
    with open(filename, 'w') as fp:
        for name in tests:
            print('Lib/test/%s.py' % name, file=fp)
    output = self.run_tests('--fromfile', filename)
    self.check_executed_tests(output, tests)
