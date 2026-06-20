# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poll.py
# case: PollTests_test_poll1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = select.poll()
    NUM_PIPES = 12
    MSG = b' This is a test.'
    MSG_LEN = len(MSG)
    readers = []
    writers = []
    r2w = {}
    w2r = {}
    for i in range(NUM_PIPES):
        (rd, wr) = os.pipe()
        p.register(rd)
        p.modify(rd, select.POLLIN)
        p.register(wr, select.POLLOUT)
        readers.append(rd)
        writers.append(wr)
        r2w[rd] = wr
        w2r[wr] = rd
    bufs = []
    while writers:
        ready = p.poll()
        ready_writers = find_ready_matching(ready, select.POLLOUT)
        if not ready_writers:
            raise RuntimeError('no pipes ready for writing')
        wr = random.choice(ready_writers)
        os.write(wr, MSG)
        ready = p.poll()
        ready_readers = find_ready_matching(ready, select.POLLIN)
        if not ready_readers:
            raise RuntimeError('no pipes ready for reading')
        rd = random.choice(ready_readers)
        buf = os.read(rd, MSG_LEN)
        self.assertEqual(len(buf), MSG_LEN)
        bufs.append(buf)
        os.close(r2w[rd])
        os.close(rd)
        p.unregister(r2w[rd])
        p.unregister(rd)
        writers.remove(r2w[rd])
    self.assertEqual(bufs, [MSG] * NUM_PIPES)
