# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_send_recv_different_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()

    def f():
        while True:
            try:
                obj = interpreters.channel_recv(cid)
                break
            except interpreters.ChannelEmptyError:
                time.sleep(0.1)
        interpreters.channel_send(cid, obj)
    t = threading.Thread(target=f)
    t.start()
    interpreters.channel_send(cid, b'spam')
    t.join()
    obj = interpreters.channel_recv(cid)
    self.assertEqual(obj, b'spam')
