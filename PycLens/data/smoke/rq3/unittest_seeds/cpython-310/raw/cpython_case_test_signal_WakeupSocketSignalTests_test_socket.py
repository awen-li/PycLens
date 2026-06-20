# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupSocketSignalTests_test_socket

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n        import signal\n        import socket\n        import struct\n        import _testcapi\n\n        signum = signal.SIGINT\n        signals = (signum,)\n\n        def handler(signum, frame):\n            pass\n\n        signal.signal(signum, handler)\n\n        read, write = socket.socketpair()\n        write.setblocking(False)\n        signal.set_wakeup_fd(write.fileno())\n\n        signal.raise_signal(signum)\n\n        data = read.recv(1)\n        if not data:\n            raise Exception("no signum written")\n        raised = struct.unpack(\'B\', data)\n        if raised != signals:\n            raise Exception("%r != %r" % (raised, signals))\n\n        read.close()\n        write.close()\n        '
    assert_python_ok('-c', code)
