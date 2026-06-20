# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: HandlerTest_test_path_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (fd, fn) = tempfile.mkstemp()
    os.close(fd)
    os.unlink(fn)
    pfn = pathlib.Path(fn)
    cases = ((logging.FileHandler, (pfn, 'w')), (logging.handlers.RotatingFileHandler, (pfn, 'a')), (logging.handlers.TimedRotatingFileHandler, (pfn, 'h')))
    if sys.platform in ('linux', 'darwin'):
        cases += ((logging.handlers.WatchedFileHandler, (pfn, 'w')),)
    for (cls, args) in cases:
        h = cls(*args, encoding='utf-8')
        self.assertTrue(os.path.exists(fn))
        h.close()
        os.unlink(fn)
