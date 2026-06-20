# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_compiler_recursion_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fail_depth = sys.getrecursionlimit() * 3
    crash_depth = sys.getrecursionlimit() * 300
    success_depth = int(fail_depth * 0.75)

    def check_limit(prefix, repeated, mode='single'):
        expect_ok = prefix + repeated * success_depth
        compile(expect_ok, '<test>', mode)
        for depth in (fail_depth, crash_depth):
            broken = prefix + repeated * depth
            details = 'Compiling ({!r} + {!r} * {})'.format(prefix, repeated, depth)
            with self.assertRaises(RecursionError, msg=details):
                compile(broken, '<test>', mode)
    check_limit('a', '()')
    check_limit('a', '.b')
    check_limit('a', '[0]')
    check_limit('a', '*a')
