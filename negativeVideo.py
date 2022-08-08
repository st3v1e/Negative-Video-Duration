import sys

if len(sys.argv) < 2:
    print("Need video file (mp4)")
    exit(0)

with open(sys.argv[1], 'r+b') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('6D766864'))
    f.seek(offset + 16)
    f.write(bytes.fromhex('00000001FFFFFFF0'))
    
# test