# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_fsize_enforced

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        (cur, max) = resource.getrlimit(resource.RLIMIT_FSIZE)
    except AttributeError:
        pass
    else:
        try:
            try:
                resource.setrlimit(resource.RLIMIT_FSIZE, (1024, max))
                limit_set = True
            except ValueError:
                limit_set = False
            f = open(os_helper.TESTFN, 'wb')
            try:
                f.write(b'X' * 1024)
                try:
                    f.write(b'Y')
                    f.flush()
                    for i in range(5):
                        time.sleep(0.1)
                        f.flush()
                except OSError:
                    if not limit_set:
                        raise
                if limit_set:
                    resource.setrlimit(resource.RLIMIT_FSIZE, (cur, max))
            finally:
                f.close()
        finally:
            if limit_set:
                resource.setrlimit(resource.RLIMIT_FSIZE, (cur, max))
            os_helper.unlink(os_helper.TESTFN)
