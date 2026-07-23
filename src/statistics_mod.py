class Stats():
    def __init__(self,sequences,orf,protein):
        self.seqsana = len(sequences)
        self.orfs = len(orf)
        self.prots = len(protein)

def log_main(orf,protein,sequences):
    stat = Stats(sequences,orf,protein)
    return stat