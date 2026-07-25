def validate(sequence,bases = {'A','T','G','C','U'}):
    if len(sequence) == 0:
        return False
    for base in sequence:
        if base not in bases:
            return False
    if 'U' in sequence and 'T' in sequence:
        return False
    return True

def clean(sequence):
    seq = "".join(sequence.upper().split())
    seq = seq.replace("-", "").replace(",", "")
    return seq