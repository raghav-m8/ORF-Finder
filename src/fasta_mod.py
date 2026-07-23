from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

class Sequence:
        def __init__(self,sequence_id,seq,desc):
            self.id = sequence_id
            self.seq = seq
            self.desc = desc

def fasta_parser(address):
    try:
        sequences = []
        for record in SeqIO.parse(address,'fasta'):
            sequence_obj = Sequence(
                str(record.id),
                str(record.seq),
                str(record.description)
            )
            sequences.append(sequence_obj)
        return sequences
    except Exception as e:
        print(e)

def fasta_orf(orfs):
    with open("orf_output.fasta","w") as output:
        for orf in orfs:
            sign = "+" if orf.sense else "-" 
            record = SeqRecord(
                Seq(orf.orf),
                id = orf.data.id,
                description = "ORF " + str(orf.num) + " | " + "RF: " + sign + str(orf.rf)
            )
            SeqIO.write(record,output,'fasta')
def fasta_prot(prots):
    with open("protein_output.fasta","w") as output:
        for protein in prots:
            sign = "+" if protein.sense else "-" 
            record = SeqRecord(
                    Seq(protein.seq),
                    id = protein.data.id,
                    description = "ORF " + str(protein.num) + " | " + "RF: " + sign + str(protein.rf)
                )
            SeqIO.write(record,output,'fasta')
        