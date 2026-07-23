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

def giveout(inp):
    choices = []
    i = int(inp.replace(",","").replace(" ",""))
    while i != 0:
        choices.append(i%10)
        i = i//10
    return choices

def output(choices,orfs,proteins,stats):
    for i in choices:
        if i == 1: fasta_orf(orfs)
        elif i == 2: fasta_prot(proteins)
        elif i == 3: txt(stats)
        elif i == 4:  
            fasta_orf(orfs)
            fasta_prot(proteins)
            txt(stats)
        elif i == 5: print("Program Exited")
    
def txt(stat):
    txt = []
    txt.append("="*80 + "\n"
                + "QUICK REPORT".center(80) + "\n"
                + "="*80 + "\n"
            )
    txt.append(f"Sequences Analysed: {stat.seqsana}\n")
    txt.append(f"ORFs Found: {stat.orfs}\n")
    txt.append(f"Proteins Found: {stat.prots}\n")
    with open("Analysis Report.txt","w") as report:
        report.write("".join(txt))
        

