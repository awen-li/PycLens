# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poll.py
# case: PollTests_test_poll2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmd = 'for i in 0 1 2 3 4 5 6 7 8 9; do echo testing...; sleep 1; done'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=0)
    proc.__enter__()
    self.addCleanup(proc.__exit__, None, None, None)
    p = proc.stdout
    pollster = select.poll()
    pollster.register(p, select.POLLIN)
    for tout in (0, 1000, 2000, 4000, 8000, 16000) + (-1,) * 10:
        fdlist = pollster.poll(tout)
        if fdlist == []:
            continue
        (fd, flags) = fdlist[0]
        if flags & select.POLLHUP:
            line = p.readline()
            if line != b'':
                self.fail('error: pipe seems to be closed, but still returns data')
            continue
        elif flags & select.POLLIN:
            line = p.readline()
            if not line:
                break
            self.assertEqual(line, b'testing...\n')
            continue
        else:
            self.fail('Unexpected return value from select.poll: %s' % fdlist)
