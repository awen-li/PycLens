# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_kqueue.py
# case: TestKQueue_test_queue_event

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    serverSocket = socket.create_server(('127.0.0.1', 0))
    client = socket.socket()
    client.setblocking(False)
    try:
        client.connect(('127.0.0.1', serverSocket.getsockname()[1]))
    except OSError as e:
        self.assertEqual(e.args[0], errno.EINPROGRESS)
    else:
        pass
    (server, addr) = serverSocket.accept()
    kq = select.kqueue()
    kq2 = select.kqueue.fromfd(kq.fileno())
    ev = select.kevent(server.fileno(), select.KQ_FILTER_WRITE, select.KQ_EV_ADD | select.KQ_EV_ENABLE)
    kq.control([ev], 0)
    ev = select.kevent(server.fileno(), select.KQ_FILTER_READ, select.KQ_EV_ADD | select.KQ_EV_ENABLE)
    kq.control([ev], 0)
    ev = select.kevent(client.fileno(), select.KQ_FILTER_WRITE, select.KQ_EV_ADD | select.KQ_EV_ENABLE)
    kq2.control([ev], 0)
    ev = select.kevent(client.fileno(), select.KQ_FILTER_READ, select.KQ_EV_ADD | select.KQ_EV_ENABLE)
    kq2.control([ev], 0)
    events = kq.control(None, 4, 1)
    events = set(((e.ident, e.filter) for e in events))
    self.assertEqual(events, set([(client.fileno(), select.KQ_FILTER_WRITE), (server.fileno(), select.KQ_FILTER_WRITE)]))
    client.send(b'Hello!')
    server.send(b'world!!!')
    for i in range(10):
        events = kq.control(None, 4, 1)
        if len(events) == 4:
            break
        time.sleep(1.0)
    else:
        self.fail('timeout waiting for event notifications')
    events = set(((e.ident, e.filter) for e in events))
    self.assertEqual(events, set([(client.fileno(), select.KQ_FILTER_WRITE), (client.fileno(), select.KQ_FILTER_READ), (server.fileno(), select.KQ_FILTER_WRITE), (server.fileno(), select.KQ_FILTER_READ)]))
    ev = select.kevent(client.fileno(), select.KQ_FILTER_WRITE, select.KQ_EV_DELETE)
    kq.control([ev], 0)
    ev = select.kevent(client.fileno(), select.KQ_FILTER_READ, select.KQ_EV_DELETE)
    kq.control([ev], 0)
    ev = select.kevent(server.fileno(), select.KQ_FILTER_READ, select.KQ_EV_DELETE)
    kq.control([ev], 0, 0)
    events = kq.control([], 4, 0.99)
    events = set(((e.ident, e.filter) for e in events))
    self.assertEqual(events, set([(server.fileno(), select.KQ_FILTER_WRITE)]))
    client.close()
    server.close()
    serverSocket.close()
