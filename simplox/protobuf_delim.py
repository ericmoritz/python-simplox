
class VarIntDecoder(object):
    """
    Use this with whatever byte source you have
    """
    def __init__(self):
        self.__val = 0
        self.__depth = 0
    
    def feed(self, byte):
        byte_int = ord(byte)

        msb = byte_int >> 7
        i   = byte_int & 127
        self.__val = i << self.__depth | self.__val
        if msb == 0:
            return self.__val
        else:
            self.__depth += 7

        
class LazyChunkedReader(object):
    """
    This enable a file-like interface to a chunked iterator.
    Useful for iterating over requests.Response chunks
    """
    def __init__(self, chunk_iter):
        self.__iter = chunk_iter
        self.__cursor = 0
        self.__buffer = ""

    def read(self, size):
        self._accumulate_until(size)
        ret = self.__buffer[:size]
        self.__buffer = self.__buffer[size:]
        return ret

    def _accumulate_until(self, size):
        while len(self.__buffer) < size:
            try:
                self.__buffer += self.__iter.next()
            except StopIteration:
                return # we can't consume any more
                

def delimited(fh):
    decoder = VarIntDecoder()
    byte = fh.read(1)
    while byte:
        size = decoder.feed(byte)
        if size is not None:
            decoder = VarIntDecoder()
            yield fh.read(size)
        byte = fh.read(1)

        
