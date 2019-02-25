import sys

def zlib_decompress(buffer ,target_path):
    try:
        import zlib
    except ImportError:
        print("Cannot import zlib")
        return None
    with open(target_path, 'wb') as handle:
        handle.write(zlib.decompress(buffer, zlib.MAX_WBITS))
    
def locate_zlib_offset(buffer):
    zlib_headers = [b'\x78\x9c', b'\x78\x01', b'\x78\xda']
    #list comprehension version
    #[e for e in [buffer.find(header) for header in zlib_headers] if e > 0] 
    for header in zlib_headers:
        offset = buffer.find(header)
        print(offset)
        if offset != -1:
            return offset
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NZ Decompress')
    parser.add_argument('-f','--file', required=True, help='Input file')
    parser.add_argument('-o','--output', required=True, help='Output file')
    args = parser.parse_args()
    with open(args.file, 'rb') as fp:
        buffer = fp.read()
    offset = locate_zlib_offset(buffer)
    if offset:
        #found a zlib header
        zlib_decompress(buffer[offset:], args.output)
