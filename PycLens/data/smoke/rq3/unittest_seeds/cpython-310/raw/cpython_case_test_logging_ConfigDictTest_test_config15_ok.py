# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_config15_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cleanup(h1, fn):
        h1.close()
        os.remove(fn)
    with self.check_no_resource_warning():
        (fd, fn) = tempfile.mkstemp('.log', 'test_logging-X-')
        os.close(fd)
        config = {'version': 1, 'handlers': {'file': {'class': 'logging.FileHandler', 'filename': fn, 'encoding': 'utf-8'}}, 'root': {'handlers': ['file']}}
        self.apply_config(config)
        self.apply_config(config)
    handler = logging.root.handlers[0]
    self.addCleanup(cleanup, handler, fn)
