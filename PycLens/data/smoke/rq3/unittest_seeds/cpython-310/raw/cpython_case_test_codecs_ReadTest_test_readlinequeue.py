# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ReadTest_test_readlinequeue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = Queue(b'')
    writer = codecs.getwriter(self.encoding)(q)
    reader = codecs.getreader(self.encoding)(q)
    writer.write('foo\r')
    self.assertEqual(reader.readline(keepends=False), 'foo')
    writer.write('\nbar\r')
    self.assertEqual(reader.readline(keepends=False), '')
    self.assertEqual(reader.readline(keepends=False), 'bar')
    writer.write('baz')
    self.assertEqual(reader.readline(keepends=False), 'baz')
    self.assertEqual(reader.readline(keepends=False), '')
    writer.write('foo\r')
    self.assertEqual(reader.readline(keepends=True), 'foo\r')
    writer.write('\nbar\r')
    self.assertEqual(reader.readline(keepends=True), '\n')
    self.assertEqual(reader.readline(keepends=True), 'bar\r')
    writer.write('baz')
    self.assertEqual(reader.readline(keepends=True), 'baz')
    self.assertEqual(reader.readline(keepends=True), '')
    writer.write('foo\r\n')
    self.assertEqual(reader.readline(keepends=True), 'foo\r\n')
