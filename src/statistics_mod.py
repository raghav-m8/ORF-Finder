class genStat():
    def __init__(self,sequences,orf,protein):
        self.seqsana = len(sequences)
        self.orfs = len(orf)
        self.nvalid = sum(sequence.valid for sequence in sequences)
        self.prots = len(protein)
class SeqStat():
    def __init__(self,valid,length,gc,desc,seqid,num_of_orfs,orf_lst):
        self.valid = valid
        self.length = length
        self.gcc = gc
        self.desc = desc
        self.id = seqid
        self.norfs = num_of_orfs
        self.orf_lst = orf_lst

def log_main(orf,proteins,sequences):
    gen_stat = genStat(sequences,orf,proteins)
    individual_stats = log_indiv(sequences,orf,proteins)
    return gen_stat,individual_stats

def log_indiv(sequences,orfs,proteins):
    sequence_stats = []
    orf_stats = []
    protein_stats =[]
    for sequence in sequences:
        orf_lst = []
        count = 0
        for count_orf in orfs:
            if count_orf.id==sequence.id:
                count+=1
                orf_lst.append(count_orf)
        sequence_stat = SeqStat(
            sequence.valid,
            len(sequence.seq),
            sequence.gc,
            sequence.desc,
            sequence.id,
            count,
            orf_lst
        )
        sequence_stats.append(sequence_stat)
    return sequence_stats