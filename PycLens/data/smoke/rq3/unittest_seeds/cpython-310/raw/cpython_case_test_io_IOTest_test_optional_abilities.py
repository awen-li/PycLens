# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_optional_abilities

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def pipe_reader():
        [r, w] = os.pipe()
        os.close(w)
        return self.FileIO(r, 'r')

    def pipe_writer():
        [r, w] = os.pipe()
        self.addCleanup(os.close, r)
        thread = threading.Thread(target=os.read, args=(r, 100))
        thread.start()
        self.addCleanup(thread.join)
        return self.FileIO(w, 'w')

    def buffered_reader():
        return self.BufferedReader(self.MockUnseekableIO())

    def buffered_writer():
        return self.BufferedWriter(self.MockUnseekableIO())

    def buffered_random():
        return self.BufferedRandom(self.BytesIO())

    def buffered_rw_pair():
        return self.BufferedRWPair(self.MockUnseekableIO(), self.MockUnseekableIO())

    def text_reader():

        class UnseekableReader(self.MockUnseekableIO):
            writable = self.BufferedIOBase.writable
            write = self.BufferedIOBase.write
        return self.TextIOWrapper(UnseekableReader(), 'ascii')

    def text_writer():

        class UnseekableWriter(self.MockUnseekableIO):
            readable = self.BufferedIOBase.readable
            read = self.BufferedIOBase.read
        return self.TextIOWrapper(UnseekableWriter(), 'ascii')
    tests = ((pipe_reader, 'fr'), (pipe_writer, 'fw'), (buffered_reader, 'r'), (buffered_writer, 'w'), (buffered_random, 'rws'), (buffered_rw_pair, 'rw'), (text_reader, 'r'), (text_writer, 'w'), (self.BytesIO, 'rws'), (self.StringIO, 'rws'))
    for [test, abilities] in tests:
        with self.subTest(test), test() as obj:
            readable = 'r' in abilities
            self.assertEqual(obj.readable(), readable)
            writable = 'w' in abilities
            self.assertEqual(obj.writable(), writable)
            if isinstance(obj, self.TextIOBase):
                data = '3'
            elif isinstance(obj, (self.BufferedIOBase, self.RawIOBase)):
                data = b'3'
            else:
                self.fail('Unknown base class')
            if 'f' in abilities:
                obj.fileno()
            else:
                self.assertRaises(OSError, obj.fileno)
            if readable:
                obj.read(1)
                obj.read()
            else:
                self.assertRaises(OSError, obj.read, 1)
                self.assertRaises(OSError, obj.read)
            if writable:
                obj.write(data)
            else:
                self.assertRaises(OSError, obj.write, data)
            if sys.platform.startswith('win') and test in (pipe_reader, pipe_writer):
                continue
            seekable = 's' in abilities
            self.assertEqual(obj.seekable(), seekable)
            if seekable:
                obj.tell()
                obj.seek(0)
            else:
                self.assertRaises(OSError, obj.tell)
                self.assertRaises(OSError, obj.seek, 0)
            if writable and seekable:
                obj.truncate()
                obj.truncate(0)
            else:
                self.assertRaises(OSError, obj.truncate)
                self.assertRaises(OSError, obj.truncate, 0)
