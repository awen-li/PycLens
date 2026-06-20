# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poll.py
# case: PollTests_test_poll_unit_tests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (FD, w) = os.pipe()
    os.close(FD)
    os.close(w)
    p = select.poll()
    p.register(FD)
    r = p.poll()
    self.assertEqual(r[0], (FD, select.POLLNVAL))
    with open(TESTFN, 'w') as f:
        fd = f.fileno()
        p = select.poll()
        p.register(f)
        r = p.poll()
        self.assertEqual(r[0][0], fd)
    r = p.poll()
    self.assertEqual(r[0], (fd, select.POLLNVAL))
    os.unlink(TESTFN)
    p = select.poll()
    self.assertRaises(TypeError, p.register, p)
    self.assertRaises(TypeError, p.unregister, p)
    p = select.poll()
    self.assertRaises(KeyError, p.unregister, 3)
    pollster = select.poll()

    class Nope:
        pass

    class Almost:

        def fileno(self):
            return 'fileno'
    self.assertRaises(TypeError, pollster.register, Nope(), 0)
    self.assertRaises(TypeError, pollster.register, Almost(), 0)
