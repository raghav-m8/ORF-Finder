from fasta_mod import fasta_orf
from fasta_mod import fasta_prot

def report():
    pass

def start():
    print("=" * 40)
    print("ORF FINDER")
    print("=" * 40)
    print("1. Analyse FASTA File"),print("2.Exit")  
    init = int(input("Choice: "))
    return True if init == 1 else False 

def ready():
    print("Analysis Complete")
    print("Select Analysis Output" + "\n"
            + "1.ORF FASTA" + "\n"
            + "2.Protein FASTA" + "\n"
            + "3.Analysis Report" + "\n"
            + "4.Extract All" + "\n"
            + "5.Exit")
    return giveout((input("Choice: ")))

def minlen():
    return int(input("Minimum ORF length (bp): "))

def giveout(inp):
    choices = []
    i = int(inp.replace(",","").replace(" ",""))
    while i != 0:
        choices.append(i%10)
        i = i//10
    return choices

def output(choices,orfs,proteins,gen_stats,seq_stats):
    for i in choices:
        if i == 1: fasta_orf(orfs)
        elif i == 2: fasta_prot(proteins)
        elif i == 3: txt(gen_stats,seq_stats)
        elif i == 4:  
            fasta_orf(orfs)
            fasta_prot(proteins)
            txt(gen_stats,seq_stats)
        elif i == 5: print("Program Exited")
    
def txt(gen_stats,seq_stats):
    txt = []
    txt.append("="*80 + "\n"
                + "ANALYSIS REPORT".center(80) + "\n"
                + "="*80 + "\n"
            )
    for seq_stat in seq_stats:
        txt.append(f"Sequence ID: {seq_stat.id}\n")
        txt.append(f"Sequence Description: {seq_stat.desc}\n")
        txt.append(f"Sequence Length: {seq_stat.length}bp\n")
        txt.append(f"Sequence GC Content(%): {seq_stat.gcc}%\n")
        txt.append(f"Number of ORFs found in {seq_stat.id}: {seq_stat.norfs}\n")
        txt.append("-"*80)
    txt.append("="*80)
    txt.append(f"Sequences Analysed: {gen_stats.seqsana}\n")
    txt.append(f"Valid Sequences: {gen_stats.nvalid}\n")
    txt.append(f"ORFs Found: {gen_stats.orfs}\n")
    txt.append(f"Proteins Found: {gen_stats.prots}\n")
    with open("Analysis Report.txt","w") as report:
        report.write("".join(txt))

