# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: StdPrinterTests_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    message = 'unicode:é-€-\udc80!\n'
    stdout_fd = self.STDOUT_FD
    stdout_fd_copy = os.dup(stdout_fd)
    self.addCleanup(os.close, stdout_fd_copy)
    (rfd, wfd) = os.pipe()
    self.addCleanup(os.close, rfd)
    self.addCleanup(os.close, wfd)
    try:
        os.dup2(wfd, stdout_fd)
        printer = self.create_printer(stdout_fd)
        printer.write(message)
    finally:
        os.dup2(stdout_fd_copy, stdout_fd)
    data = os.read(rfd, 100)
    self.assertEqual(data, message.encode('utf8', 'backslashreplace'))
