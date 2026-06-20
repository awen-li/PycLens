# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_release

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = bytearray([1, 2, 3])
    m = memoryview(a)
    nd = ndarray(m)
    self.assertRaises(BufferError, m.release)
    del nd
    m.release()
    a = bytearray([1, 2, 3])
    m = memoryview(a)
    nd1 = ndarray(m, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    nd2 = ndarray(nd1, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    self.assertIs(nd2.obj, m)
    self.assertRaises(BufferError, m.release)
    del nd1, nd2
    m.release()
    a = bytearray([1, 2, 3])
    m1 = memoryview(a)
    m2 = memoryview(m1)
    nd = ndarray(m2)
    m1.release()
    self.assertRaises(BufferError, m2.release)
    del nd
    m2.release()
    a = bytearray([1, 2, 3])
    m1 = memoryview(a)
    m2 = memoryview(m1)
    nd1 = ndarray(m2, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    nd2 = ndarray(nd1, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    self.assertIs(nd2.obj, m2)
    m1.release()
    self.assertRaises(BufferError, m2.release)
    del nd1, nd2
    m2.release()
    nd = ndarray([1, 2, 3], shape=[3], flags=ND_VAREXPORT)
    m1 = memoryview(nd)
    nd.push([4, 5, 6, 7, 8], shape=[5])
    m2 = memoryview(nd)
    x = memoryview(m1)
    self.assertEqual(x.tolist(), m1.tolist())
    y = memoryview(m2)
    self.assertEqual(y.tolist(), m2.tolist())
    self.assertEqual(y.tolist(), nd.tolist())
    m2.release()
    y.release()
    nd.pop()
    self.assertEqual(x.tolist(), nd.tolist())
    del nd
    m1.release()
    x.release()

    def catch22(b):
        with memoryview(b) as m2:
            pass
    x = bytearray(b'123')
    with memoryview(x) as m1:
        catch22(m1)
        self.assertEqual(m1[0], ord(b'1'))
    x = ndarray(list(range(12)), shape=[2, 2, 3], format='l')
    y = ndarray(x, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    z = ndarray(y, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    self.assertIs(z.obj, x)
    with memoryview(z) as m:
        catch22(m)
        self.assertEqual(m[0:1].tolist(), [[[0, 1, 2], [3, 4, 5]]])
    for flags in (0, ND_REDIRECT):
        x = bytearray(b'123')
        with memoryview(x) as m1:
            del x
            y = ndarray(m1, getbuf=PyBUF_FULL_RO, flags=flags)
            with memoryview(y) as m2:
                del y
                z = ndarray(m2, getbuf=PyBUF_FULL_RO, flags=flags)
                with memoryview(z) as m3:
                    del z
                    catch22(m3)
                    catch22(m2)
                    catch22(m1)
                    self.assertEqual(m1[0], ord(b'1'))
                    self.assertEqual(m2[1], ord(b'2'))
                    self.assertEqual(m3[2], ord(b'3'))
                    del m3
                del m2
            del m1
        x = bytearray(b'123')
        with memoryview(x) as m1:
            del x
            y = ndarray(m1, getbuf=PyBUF_FULL_RO, flags=flags)
            with memoryview(y) as m2:
                del y
                z = ndarray(m2, getbuf=PyBUF_FULL_RO, flags=flags)
                with memoryview(z) as m3:
                    del z
                    catch22(m1)
                    catch22(m2)
                    catch22(m3)
                    self.assertEqual(m1[0], ord(b'1'))
                    self.assertEqual(m2[1], ord(b'2'))
                    self.assertEqual(m3[2], ord(b'3'))
                    del m1, m2, m3
    x = bytearray(b'123')
    with self.assertRaises(BufferError):
        with memoryview(x) as m:
            ex = ndarray(m)
            m[0] == ord(b'1')
