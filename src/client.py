import socket
import argparse as ap


def coords(s):
    try:
        x, y = map(int, s.split(","))
        return x, y
    except:
        print("error in coords")


endl = '\r\n'
parser = ap.ArgumentParser(description="Client To Test Ex4 in Advanced programming")
parser.add_argument("-p", default=8081, type=int, help="port to use")
parser.add_argument("-a", default="A*", choices=["A*", "BFS", "DFS", "BestFS"],
                    help="the algorithm to ask the server to use, default A*")
parser.add_argument("-s", default=(0, 0), type=coords, help="starting point separated by comma")
parser.add_argument("-e", default=(-1, -1), type=coords, help="ending point separated by comma")
args = parser.parse_args()
port = args.p
algorithm = args.a

sock = socket.socket()
sock.connect(("127.0.0.1", port))
sock.send(b"solve find-graph-path {algorithm}{endl*2}")
print(sock.recv(1000).decode())

with open('matrix', 'r') as f:
    mat = [[float(num) for num in line.split(',')] for line in f]
height = len(mat)
width = len(mat[0])
matString = ''
for i in range(height):
    for j in range(width - 1):
        matString += str(mat[i][j]) + ','
    matString += str(mat[i][width - 1])
    if i != height - 1:
        matString += endl
startingPoint = '' + str(args.s[0]) + ',' + str(args.s[1])
endingPoint = f'{height - 1},{width - 1}'
if args.e[0] != -1:
    endingPoint = '' + str(args.e[0]) + ',' + str(args.e[1])

message = b"{matString}{endl}{startingPoint}{endl}{endingPoint}{endl*2}"
sock = socket.socket()
sock.connect(("127.0.0.1", port))
sock.send(message)
print(sock.recv(1000).decode())
