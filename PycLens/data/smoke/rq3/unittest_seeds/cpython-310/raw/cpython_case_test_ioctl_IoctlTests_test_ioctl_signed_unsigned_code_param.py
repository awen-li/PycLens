# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ioctl.py
# case: IoctlTests_test_ioctl_signed_unsigned_code_param

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not pty:
        raise unittest.SkipTest('pty module required')
    (mfd, sfd) = pty.openpty()
    try:
        if termios.TIOCSWINSZ < 0:
            set_winsz_opcode_maybe_neg = termios.TIOCSWINSZ
            set_winsz_opcode_pos = termios.TIOCSWINSZ & 4294967295
        else:
            set_winsz_opcode_pos = termios.TIOCSWINSZ
            (set_winsz_opcode_maybe_neg,) = struct.unpack('i', struct.pack('I', termios.TIOCSWINSZ))
        our_winsz = struct.pack('HHHH', 80, 25, 0, 0)
        new_winsz = fcntl.ioctl(mfd, set_winsz_opcode_pos, our_winsz)
        new_winsz = fcntl.ioctl(mfd, set_winsz_opcode_maybe_neg, our_winsz)
    finally:
        os.close(mfd)
        os.close(sfd)
