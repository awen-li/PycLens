# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_testfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    SKIP_ON_TIGER = {'tan0064'}
    osx_version = None
    if sys.platform == 'darwin':
        version_txt = platform.mac_ver()[0]
        try:
            osx_version = tuple(map(int, version_txt.split('.')))
        except ValueError:
            pass
    fail_fmt = '{}: {}({!r}): {}'
    failures = []
    for (id, fn, ar, ai, er, ei, flags) in parse_testfile(test_file):
        if ai != 0.0 or ei != 0.0:
            continue
        if fn in ['rect', 'polar']:
            continue
        if osx_version is not None and osx_version < (10, 5):
            if id in SKIP_ON_TIGER:
                continue
        func = getattr(math, fn)
        if 'invalid' in flags or 'divide-by-zero' in flags:
            er = 'ValueError'
        elif 'overflow' in flags:
            er = 'OverflowError'
        try:
            result = func(ar)
        except ValueError:
            result = 'ValueError'
        except OverflowError:
            result = 'OverflowError'
        (ulp_tol, abs_tol) = (5, 0.0)
        failure = result_check(er, result, ulp_tol, abs_tol)
        if failure is None:
            continue
        msg = fail_fmt.format(id, fn, ar, failure)
        failures.append(msg)
    if failures:
        self.fail('Failures in test_testfile:\n  ' + '\n  '.join(failures))
