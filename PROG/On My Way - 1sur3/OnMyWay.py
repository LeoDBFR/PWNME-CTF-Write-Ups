import pwn

HOST = "prog.pwnme.fr"
PORT = 7000

p = pwn.remote(HOST, PORT)

def recuperer(data):
    layers = [x.strip() for x in data.split(b"\n-\n")]
    if b"Answer" in layers[-1]:
        return [matrix.split(b"\n") for matrix in layers[:-1]]
    else:
        return layers

def solve(layers):
    pos_s = None
    pos_e = None
    for i_z, layer in enumerate(layers):
        for i_y, line in enumerate(layer):
            for i_x, char in enumerate(line):
                truc = (i_x, i_y, i_z)
                char = chr(char).encode()
                print(truc, char)
                if char == b"S":
                    pos_s = truc
                elif char == b"E":
                    pos_e = truc
                if pos_s and pos_e: break
            if pos_s and pos_e: break
        if pos_s and pos_e: break
    print("S:", pos_s)
    print("E:", pos_e)
    if pos_s and pos_e:
        val = abs(pos_s[0] - pos_e[0])
        val += abs(pos_s[1] - pos_e[1])
        val += abs(pos_s[2] - pos_e[2])
        return val
    else:
        return None

def main():
    while True:
        try:
            data = p.recvuntil(b">> ", timeout=10)
        except EOFError:
            print(p.recvall(timeout=2))
            p.close()
            break
        print(data)
        layers = recuperer(data)
        if len(layers) > 1:
            result=solve(layers)
            print("Resultat:", result)
            if not result:
                print("erreur du résultat")
                return
            p.sendline(str(result).encode())
        else:
            break

main()
