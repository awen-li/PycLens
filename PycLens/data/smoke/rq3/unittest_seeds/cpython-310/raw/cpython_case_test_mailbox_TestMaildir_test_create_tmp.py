# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_create_tmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hostname = socket.gethostname()
    if '/' in hostname:
        hostname = hostname.replace('/', '\\057')
    if ':' in hostname:
        hostname = hostname.replace(':', '\\072')
    pid = os.getpid()
    pattern = re.compile('(?P<time>\\d+)\\.M(?P<M>\\d{1,6})P(?P<P>\\d+)Q(?P<Q>\\d+)\\.(?P<host>[^:/]*)')
    previous_groups = None
    for x in range(repetitions):
        tmp_file = self._box._create_tmp()
        (head, tail) = os.path.split(tmp_file.name)
        self.assertEqual(head, os.path.abspath(os.path.join(self._path, 'tmp')), "File in wrong location: '%s'" % head)
        match = pattern.match(tail)
        self.assertIsNotNone(match, "Invalid file name: '%s'" % tail)
        groups = match.groups()
        if previous_groups is not None:
            self.assertGreaterEqual(int(groups[0]), int(previous_groups[0]), "Non-monotonic seconds: '%s' before '%s'" % (previous_groups[0], groups[0]))
            if int(groups[0]) == int(previous_groups[0]):
                self.assertGreaterEqual(int(groups[1]), int(previous_groups[1]), "Non-monotonic milliseconds: '%s' before '%s'" % (previous_groups[1], groups[1]))
            self.assertEqual(int(groups[2]), pid, "Process ID mismatch: '%s' should be '%s'" % (groups[2], pid))
            self.assertEqual(int(groups[3]), int(previous_groups[3]) + 1, "Non-sequential counter: '%s' before '%s'" % (previous_groups[3], groups[3]))
            self.assertEqual(groups[4], hostname, "Host name mismatch: '%s' should be '%s'" % (groups[4], hostname))
        previous_groups = groups
        tmp_file.write(_bytes_sample_message)
        tmp_file.seek(0)
        self.assertEqual(tmp_file.read(), _bytes_sample_message)
        tmp_file.close()
    file_count = len(os.listdir(os.path.join(self._path, 'tmp')))
    self.assertEqual(file_count, repetitions, "Wrong file count: '%s' should be '%s'" % (file_count, repetitions))
