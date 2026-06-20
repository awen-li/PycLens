# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: URandomFDTests_test_urandom_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import errno\n            import os\n            import resource\n\n            soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_NOFILE)\n            resource.setrlimit(resource.RLIMIT_NOFILE, (1, hard_limit))\n            try:\n                os.urandom(16)\n            except OSError as e:\n                assert e.errno == errno.EMFILE, e.errno\n            else:\n                raise AssertionError("OSError not raised")\n            '
    assert_python_ok('-c', code)
