# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_selector

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    NUM_SOCKETS = 12
    MSG = b' This is a test.'
    MSG_LEN = len(MSG)
    readers = []
    writers = []
    r2w = {}
    w2r = {}
    for i in range(NUM_SOCKETS):
        (rd, wr) = self.make_socketpair()
        s.register(rd, selectors.EVENT_READ)
        s.register(wr, selectors.EVENT_WRITE)
        readers.append(rd)
        writers.append(wr)
        r2w[rd] = wr
        w2r[wr] = rd
    bufs = []
    while writers:
        ready = s.select()
        ready_writers = find_ready_matching(ready, selectors.EVENT_WRITE)
        if not ready_writers:
            self.fail('no sockets ready for writing')
        wr = random.choice(ready_writers)
        wr.send(MSG)
        for i in range(10):
            ready = s.select()
            ready_readers = find_ready_matching(ready, selectors.EVENT_READ)
            if ready_readers:
                break
            sleep(0.1)
        else:
            self.fail('no sockets ready for reading')
        self.assertEqual([w2r[wr]], ready_readers)
        rd = ready_readers[0]
        buf = rd.recv(MSG_LEN)
        self.assertEqual(len(buf), MSG_LEN)
        bufs.append(buf)
        s.unregister(r2w[rd])
        s.unregister(rd)
        writers.remove(r2w[rd])
    self.assertEqual(bufs, [MSG] * NUM_SOCKETS)
