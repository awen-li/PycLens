# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_mtestfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fail_fmt = '{}: {}({!r}): {}'
    failures = []
    for (id, fn, arg, expected, flags) in parse_mtestfile(math_testcases):
        func = getattr(math, fn)
        if 'invalid' in flags or 'divide-by-zero' in flags:
            expected = 'ValueError'
        elif 'overflow' in flags:
            expected = 'OverflowError'
        try:
            got = func(arg)
        except ValueError:
            got = 'ValueError'
        except OverflowError:
            got = 'OverflowError'
        (ulp_tol, abs_tol) = (5, 0.0)
        if fn == 'gamma':
            ulp_tol = 20
        elif fn == 'lgamma':
            abs_tol = 1e-15
        elif fn == 'erfc' and arg >= 0.0:
            if arg < 1.0:
                ulp_tol = 10
            elif arg < 10.0:
                ulp_tol = 100
            else:
                ulp_tol = 1000
        failure = result_check(expected, got, ulp_tol, abs_tol)
        if failure is None:
            continue
        msg = fail_fmt.format(id, fn, arg, failure)
        failures.append(msg)
    if failures:
        self.fail('Failures in test_mtestfile:\n  ' + '\n  '.join(failures))
