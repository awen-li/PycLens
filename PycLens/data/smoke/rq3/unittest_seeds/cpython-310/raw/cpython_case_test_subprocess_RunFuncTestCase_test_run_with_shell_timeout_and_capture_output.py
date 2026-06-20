# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: RunFuncTestCase_test_run_with_shell_timeout_and_capture_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    before_secs = time.monotonic()
    try:
        subprocess.run('sleep 3', shell=True, timeout=0.1, capture_output=True)
    except subprocess.TimeoutExpired as exc:
        after_secs = time.monotonic()
        stacks = traceback.format_exc()
    else:
        self.fail('TimeoutExpired not raised.')
    self.assertLess(after_secs - before_secs, 1.5, msg=f'TimeoutExpired was delayed! Bad traceback:\n```\n{stacks}```')
