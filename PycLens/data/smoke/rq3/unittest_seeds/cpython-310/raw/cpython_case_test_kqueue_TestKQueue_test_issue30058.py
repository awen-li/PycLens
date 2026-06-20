# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_kqueue.py
# case: TestKQueue_test_issue30058

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    kq = select.kqueue()
    (a, b) = socket.socketpair()
    ev = select.kevent(a, select.KQ_FILTER_READ, select.KQ_EV_ADD | select.KQ_EV_ENABLE)
    kq.control([ev], 0)
    kq.control((ev,), 0)

    class BadList:

        def __len__(self):
            return 0

        def __iter__(self):
            for i in range(100):
                yield ev
    kq.control(BadList(), 0)
    kq.control(iter([ev]), 0)
    a.close()
    b.close()
    kq.close()
