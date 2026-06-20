# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: TimedRotatingFileHandlerTest_test_compute_files_to_delete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    wd = tempfile.mkdtemp(prefix='test_logging_')
    self.addCleanup(shutil.rmtree, wd)
    times = []
    dt = datetime.datetime.now()
    for i in range(10):
        times.append(dt.strftime('%Y-%m-%d_%H-%M-%S'))
        dt += datetime.timedelta(seconds=5)
    prefixes = ('a.b', 'a.b.c', 'd.e', 'd.e.f')
    files = []
    rotators = []
    for prefix in prefixes:
        p = os.path.join(wd, '%s.log' % prefix)
        rotator = logging.handlers.TimedRotatingFileHandler(p, when='s', interval=5, backupCount=7, delay=True)
        rotators.append(rotator)
        if prefix.startswith('a.b'):
            for t in times:
                files.append('%s.log.%s' % (prefix, t))
        else:
            rotator.namer = lambda name: name.replace('.log', '') + '.log'
            for t in times:
                files.append('%s.%s.log' % (prefix, t))
    for fn in files:
        p = os.path.join(wd, fn)
        with open(p, 'wb') as f:
            pass
    for (i, prefix) in enumerate(prefixes):
        rotator = rotators[i]
        candidates = rotator.getFilesToDelete()
        self.assertEqual(len(candidates), 3)
        if prefix.startswith('a.b'):
            p = '%s.log.' % prefix
            for c in candidates:
                (d, fn) = os.path.split(c)
                self.assertTrue(fn.startswith(p))
        else:
            for c in candidates:
                (d, fn) = os.path.split(c)
                self.assertTrue(fn.endswith('.log'))
                self.assertTrue(fn.startswith(prefix + '.') and fn[len(prefix) + 2].isdigit())
