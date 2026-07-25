from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from validator_mod import validate
from validator_mod import clean

class Sequence:
        def __init__(self,sequence_id,seq,desc,valid):
            self.id = sequence_id
            self.seq = seq
            self.desc = desc
            self.valid = valid
            self.gc = ((seq.count("G") + seq.count("C"))/len(seq)) if valid else f"Undefined as {sequence_id} is invalid"

def fasta_parser(address):
    try:
        sequences = []
        for record in SeqIO.parse(address,'fasta'):
            clean_seq = clean(str(record.seq))
            sequence_obj = Sequence(
                str(record.id),
                clean_seq,
                str(record.description),
                validate(clean_seq)
            )
            sequences.append(sequence_obj)
        return sequences
    except Exception as e:
        print(e)

def fasta_orf(orfs):
    with open("orf_output.fasta","w") as output:
        for orf in orfs:
            record = SeqRecord(
                Seq(orf.orf),
                id = orf.data.id,
                description = "ORF " + str(orf.num) + " | " + "RF: " + orf.rf
            )
            SeqIO.write(record,output,'fasta')
def fasta_prot(prots):
    with open("protein_output.fasta","w") as output:
        for protein in prots:
            record = SeqRecord(
                    Seq(protein.seq),
                    id = protein.data.id,
                    description = "ORF " + str(protein.num) + " | " + "RF: " + protein.rf
                )
            SeqIO.write(record,output,'fasta')