import math
from collections import Counter

import BWT
import MTF
from huffman import make_tree, huffman_code_tree

BLOCK_SIZES = {
    1: 1024,
    2: 2048,
    3: 4096,
    4: 8192,
    5: 16384,
    6: 32768,  # ОПАСНО - ПОЖИРАТЕЛЬ ПАМЯТИ ~ 8 Гб
    7: 65536,  # ОПАСНО - ПОЖИРАТЕЛЬ ПАМЯТИ ~10 Гб
}


def main(size_level, file_in, file_out):
    block_size = BLOCK_SIZES[size_level]
    length = 0
    encoded = []
    with open(file_in, 'rb') as f:
        alphabet = []
        for i in f.read():
            length += 1
            if i not in alphabet:
                alphabet.append(i)
        alphabet.sort()
        f.seek(0)
        blocks_count = math.ceil(length / block_size)
        packet_num = 0
        bwt_codes = []
        while True:
            print(f'Progress: {packet_num} \\ {blocks_count}')
            packet = f.read(block_size)
            if packet == b'':
                break

            bwt_step = BWT.encode(packet)
            bwt_codes.append(bwt_step[1])

            mtf_step = MTF.encode(bwt_step[0], alphabet)
            encoded.extend(mtf_step)
            packet_num += 1

    frequency = dict(Counter(encoded))
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    tree = make_tree(frequency)
    encoded_tree = huffman_code_tree(tree)
    encoded_text = [encoded_tree[i] for i in encoded]

    with open(file_out, 'wb') as f:
        for i in encoded_text:
            ch = str(i)[2:-1]
            f.write(int(ch, 2).to_bytes(math.ceil(len(ch) / 8), 'big'))


if __name__ == '__main__':
    filename = 'Rick.mp3'

    main(size_level=1, file_in=filename, file_out=f'{filename}.bin')