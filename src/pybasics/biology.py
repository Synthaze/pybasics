#
import re

AAS = {
    'R': ['R', 'Arg', 'Arginine'],
    'K': ['K', 'Lys', 'Lysine'],
    'D': ['D', 'Asp', 'Aspartate'],
    'E': ['E', 'Glu', 'Glutamate'],
    'N': ['N', 'Asn', 'Asparagine'],
    'Q': ['Q', 'Gln', 'Glutamine'],
    'S': ['S', 'Ser', 'Serine'],
    'G': ['G', 'Gly', 'Glycine'],
    'H': ['H', 'His', 'Histidine'],
    'T': ['T', 'Thr', 'Threonine'],
    'A': ['A', 'Ala', 'Alanine'],
    'P': ['P', 'Pro', 'Proline'],
    'Y': ['Y', 'Tyr', 'Tyrosine'],
    'V': ['V', 'Val', 'Valine'],
    'M': ['M', 'Met', 'Methionine'],
    'C': ['C', 'Cys', 'Cysteine'],
    'L': ['L', 'Leu', 'Leucine'],
    'F': ['F', 'Phe', 'Phenylalanine'],
    'I': ['I', 'Ile', 'Isoleucine'],
    'W': ['W', 'Trp', 'Tryptophane'],
}


def isUniprot(UniProtKB):
    return re.match(r'[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}', UniProtKB)


def isPMID(pmid):
    return re.match('[0-9]{6,8}', pmid)
