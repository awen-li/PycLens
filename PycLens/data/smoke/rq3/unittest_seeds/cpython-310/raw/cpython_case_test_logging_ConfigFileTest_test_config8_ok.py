# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigFileTest_test_config8_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cleanup(h1, fn):
        h1.close()
        os.remove(fn)
    with self.check_no_resource_warning():
        (fd, fn) = tempfile.mkstemp('.log', 'test_logging-X-')
        os.close(fd)
        if os.name == 'nt':
            fn = fn.replace('\\', '\\\\')
        config8 = self.config8.format(tempfile=fn)
        self.apply_config(config8)
        self.apply_config(config8)
    handler = logging.root.handlers[0]
    self.addCleanup(cleanup, handler, fn)
