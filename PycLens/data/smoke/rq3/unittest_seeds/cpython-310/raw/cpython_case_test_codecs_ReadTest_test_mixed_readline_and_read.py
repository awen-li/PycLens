# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ReadTest_test_mixed_readline_and_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = ['Humpty Dumpty sat on a wall,\n', 'Humpty Dumpty had a great fall.\r\n', "All the king's horses and all the king's men\r", "Couldn't put Humpty together again."]
    data = ''.join(lines)

    def getreader():
        stream = io.BytesIO(data.encode(self.encoding))
        return codecs.getreader(self.encoding)(stream)
    f = getreader()
    self.assertEqual(f.readline(), lines[0])
    self.assertEqual(f.read(), ''.join(lines[1:]))
    self.assertEqual(f.read(), '')
    f = getreader()
    self.assertEqual(f.readline(), lines[0])
    self.assertEqual(f.read(1), lines[1][0])
    self.assertEqual(f.read(0), '')
    self.assertEqual(f.read(100), data[len(lines[0]) + 1:][:100])
    f = getreader()
    self.assertEqual(f.readline(), lines[0])
    self.assertEqual(f.readlines(), lines[1:])
    self.assertEqual(f.read(), '')
    f = getreader()
    self.assertEqual(f.read(size=40, chars=5), data[:5])
    self.assertEqual(f.read(), data[5:])
    self.assertEqual(f.read(), '')
    f = getreader()
    self.assertEqual(f.read(size=40, chars=5), data[:5])
    self.assertEqual(f.read(1), data[5])
    self.assertEqual(f.read(0), '')
    self.assertEqual(f.read(100), data[6:106])
    f = getreader()
    self.assertEqual(f.read(size=40, chars=5), data[:5])
    self.assertEqual(f.readlines(), [lines[0][5:]] + lines[1:])
    self.assertEqual(f.read(), '')
