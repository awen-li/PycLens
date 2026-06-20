# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestAsynchatMocked_test_blockingioerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = unittest.mock.Mock()
    sock.recv.side_effect = BlockingIOError(errno.EAGAIN)
    dispatcher = asynchat.async_chat()
    dispatcher.set_socket(sock)
    self.addCleanup(dispatcher.del_channel)
    with unittest.mock.patch.object(dispatcher, 'handle_error') as error:
        dispatcher.handle_read()
    self.assertFalse(error.called)
