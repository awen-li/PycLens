# Source Generated with Decompyle++
# File: cpython-311-8c3236a47c21.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = None
    __pybcsec_self__ = self
    mock_socket.reply_with(b'220 Hello world')
    client = self.client()
    client.set_debuglevel(2)
    stderr = support.captured_stderr()
    client.connect(HOST, self.port)
    None(None, None)
    if None:
        with None:
            if not None:
                pass
        client.close()
        expected = re.compile('^\\d{2}:\\d{2}:\\d{2}\\.\\d{6} connect: ', re.MULTILINE)
        self.assertRegex(stderr.getvalue(), expected)
        return None

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
