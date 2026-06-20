# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: TimedRotatingFileHandlerTest_test_rollover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fh = logging.handlers.TimedRotatingFileHandler(self.fn, 'S', encoding='utf-8', backupCount=1)
    fmt = logging.Formatter('%(asctime)s %(message)s')
    fh.setFormatter(fmt)
    r1 = logging.makeLogRecord({'msg': 'testing - initial'})
    fh.emit(r1)
    self.assertLogFile(self.fn)
    time.sleep(1.1)
    r2 = logging.makeLogRecord({'msg': 'testing - after delay'})
    fh.emit(r2)
    fh.close()
    found = False
    now = datetime.datetime.now()
    GO_BACK = 5 * 60
    for secs in range(GO_BACK):
        prev = now - datetime.timedelta(seconds=secs)
        fn = self.fn + prev.strftime('.%Y-%m-%d_%H-%M-%S')
        found = os.path.exists(fn)
        if found:
            self.rmfiles.append(fn)
            break
    msg = 'No rotated files found, went back %d seconds' % GO_BACK
    if not found:
        (dn, fn) = os.path.split(self.fn)
        files = [f for f in os.listdir(dn) if f.startswith(fn)]
        print('Test time: %s' % now.strftime('%Y-%m-%d %H-%M-%S'), file=sys.stderr)
        print('The only matching files are: %s' % files, file=sys.stderr)
        for f in files:
            print('Contents of %s:' % f)
            path = os.path.join(dn, f)
            with open(path, 'r') as tf:
                print(tf.read())
    self.assertTrue(found, msg=msg)
