# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ReadTest_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def getreader(input):
        stream = io.BytesIO(input.encode(self.encoding))
        return codecs.getreader(self.encoding)(stream)

    def readalllines(input, keepends=True, size=None):
        reader = getreader(input)
        lines = []
        while True:
            line = reader.readline(size=size, keepends=keepends)
            if not line:
                break
            lines.append(line)
        return '|'.join(lines)
    s = 'foo\nbar\r\nbaz\rspam\u2028eggs'
    sexpected = 'foo\n|bar\r\n|baz\r|spam\u2028|eggs'
    sexpectednoends = 'foo|bar|baz|spam|eggs'
    self.assertEqual(readalllines(s, True), sexpected)
    self.assertEqual(readalllines(s, False), sexpectednoends)
    self.assertEqual(readalllines(s, True, 10), sexpected)
    self.assertEqual(readalllines(s, False, 10), sexpectednoends)
    lineends = ('\n', '\r\n', '\r', '\u2028')
    vw = []
    vwo = []
    for (i, lineend) in enumerate(lineends):
        vw.append((i * 200 + 200) * 'あ' + lineend)
        vwo.append((i * 200 + 200) * 'あ')
    self.assertEqual(readalllines(''.join(vw), True), '|'.join(vw))
    self.assertEqual(readalllines(''.join(vw), False), '|'.join(vwo))
    for size in range(80):
        for lineend in lineends:
            s = 10 * (size * 'a' + lineend + 'xxx\n')
            reader = getreader(s)
            for i in range(10):
                self.assertEqual(reader.readline(keepends=True), size * 'a' + lineend)
                self.assertEqual(reader.readline(keepends=True), 'xxx\n')
            reader = getreader(s)
            for i in range(10):
                self.assertEqual(reader.readline(keepends=False), size * 'a')
                self.assertEqual(reader.readline(keepends=False), 'xxx')
