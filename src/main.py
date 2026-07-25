from fasta_mod import fasta_parser
from finder_mod import find_orfs
import out_mod
from statistics_mod import log_main
from translate_mod import translate

if out_mod.start():
    file_path = str(input("Enter FASTA File Path: "))
    file_path = file_path.replace("\\","/")
    sequences = fasta_parser(file_path)
    minlen = out_mod.minlen()
    orfs = find_orfs(sequences,minlen)
    proteins = translate(orfs)
    gen_stats,seq_stats = log_main(orfs,proteins,sequences)
    choices = out_mod.ready()
    out_mod.output(choices,orfs,proteins,gen_stats,seq_stats)
   
else:
    print("Program Exited")

