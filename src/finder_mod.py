stop_codon = {'TAA','TGA','TAG'}

class ORF():
    def __init__(self,data,num,orf,rf,sense):
        self.data = data
        self.num = num
        self.orf = orf
        self.rf = rf
        self.sense = sense
        self.length = len(orf)

def find_orfs(sequences):
    orfs = []
    for sense in (True,False):
        for data in sequences:
            for rf in range(3):
                num = 0
                i = rf
                sq = reverse_complement(data.seq) if not sense else data.seq
                while i < len(sq)-1:
                    if sq[i:i+3] == 'ATG':
                        e = i + 3
                        while e <= len(sq)-1:
                            if sq[e:e+3] in stop_codon:
                                num += 1
                                orf = ORF(
                                    data,
                                    num,
                                    sq[i:e+3],
                                    rf+1,
                                    sense)
                                orfs.append(orf)
                                break
                            else: e += 3
                    i += 3
    return orfs

def reverse_complement(sequence):
    complementary_mapping = str.maketrans("ATGC","TACG")
    seq =  sequence.translate(complementary_mapping)[::-1]
    return seq