stop_codon = {'TAA','TGA','TAG'}

class ORF():
    def __init__(self,data,num,orf,rf,sense,start,end):
        self.data = data
        self.num = num
        self.orf = orf
        self.rf = f'+{rf}' if sense else f'-{rf}'
        self.length = end-start
        if sense:
            self.start = start + 1
            self.end = end
        else:
            self.start = len(data.seq)-end+1
            self.end = len(data.seq)-start

def find_orfs(sequences,minlen):
    orfs = []   
    for sense in (True,False):
        for data in sequences:
            if not data.valid:
                print(f"Sequence ID: {data.id} is invalid.")
                continue
            for rf in range(3):
                num = 0
                i = rf
                sq = reverse_complement(data.seq) if not sense else data.seq
                while i < len(sq)-1:
                    if sq[i:i+3] == 'ATG':
                        e = i + 3
                        while e <= len(sq)-1:
                            if sq[e:e+3] in stop_codon:
                                orf_seq = sq[i:e+3]
                                if e+3-i >= minlen:
                                    num += 1
                                    orf = ORF(
                                        data,
                                        num,
                                        orf_seq,
                                        rf+1,
                                        sense,
                                        i,
                                        e+3)
                                    orfs.append(orf)
                                    break
                                else:
                                    break
                            else: e += 3
                    i += 3
    return orfs

def reverse_complement(sequence):
    complementary_mapping = str.maketrans("ATGC","TACG")
    seq =  sequence.translate(complementary_mapping)[::-1]
    return seq