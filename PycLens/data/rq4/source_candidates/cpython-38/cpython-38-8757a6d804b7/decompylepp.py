# Source Generated with Decompyle++
# File: cpython-38-8757a6d804b7.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = <NODE:0>
    result = self.send_typical_request(b'GET / HTTP/1.1\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\nX-Foo: bar\r\n\r\n')
    self.assertEqual(result[0], b'HTTP/1.1 431 Too many headers\r\n')
    self.assertFalse(self.handler.get_called)
    self.assertEqual(self.handler.requestline, 'GET / HTTP/1.1')

if __name__ == '__main__':
    __pybcsec_seed__()
