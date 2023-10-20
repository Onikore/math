from pathlib import Path


class Lzw:
    def __init__(self, path):
        self.alphabet_decode = {}
        self.decode_counter = 0

        self.alphabet_encode = {}
        self.encode_counter = 0

        self.file = Path(path)
        if not self.file.is_file() or not self.file.exists():
            raise FileNotFoundError(f'File: {path}, doesnt exists')

    def create_alphabet(self, raw_text):
        for i in raw_text:
            if i not in self.alphabet_encode:
                self.alphabet_encode[i] = self.encode_counter
                self.alphabet_decode[i] = self.decode_counter
                self.encode_counter += 1
                self.decode_counter += 1
        self.alphabet_decode = {v: k for k, v in self.alphabet_decode.items()}

    def encode(self, raw_text):
        previous = ''
        encoded = []
        for current in raw_text:
            current = current
            pair = previous + current
            if pair in self.alphabet_encode:
                previous = pair
            else:
                encoded.append(self.alphabet_encode[previous])
                self.alphabet_encode[pair] = self.encode_counter
                self.encode_counter += 1
                previous = current
        if previous:
            encoded.append(self.alphabet_encode[previous])

        return encoded

    def decode(self, encoded_seq):
        decoded = []
        previous = encoded_seq.pop(0)
        decoded.append(self.alphabet_decode[previous])

        for current in encoded_seq:
            if current in self.alphabet_decode:
                entry = self.alphabet_decode[current]

            decoded.append(entry)
            self.alphabet_decode[self.decode_counter] = self.alphabet_decode[previous] + entry[0]
            self.decode_counter += 1
            previous = current
        return decoded
