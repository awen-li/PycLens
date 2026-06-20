# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: HandlerTest_test_race

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def remove_loop(fname, tries):
        for _ in range(tries):
            try:
                os.unlink(fname)
                self.deletion_time = time.time()
            except OSError:
                pass
            time.sleep(0.004 * random.randint(0, 4))
    del_count = 500
    log_count = 500
    self.handle_time = None
    self.deletion_time = None
    for delay in (False, True):
        (fd, fn) = tempfile.mkstemp('.log', 'test_logging-3-')
        os.close(fd)
        remover = threading.Thread(target=remove_loop, args=(fn, del_count))
        remover.daemon = True
        remover.start()
        h = logging.handlers.WatchedFileHandler(fn, encoding='utf-8', delay=delay)
        f = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        h.setFormatter(f)
        try:
            for _ in range(log_count):
                time.sleep(0.005)
                r = logging.makeLogRecord({'msg': 'testing'})
                try:
                    self.handle_time = time.time()
                    h.handle(r)
                except Exception:
                    print('Deleted at %s, opened at %s' % (self.deletion_time, self.handle_time))
                    raise
        finally:
            remover.join()
            h.close()
            if os.path.exists(fn):
                os.unlink(fn)
