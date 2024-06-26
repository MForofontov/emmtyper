"""
Test data
"""
import os
import shlex
from emmtyper.utilities.find import find

PROJECT_FOLDER=os.path.dirname(os.path.dirname(__file__))

test_null = "this is a null test"

primer_path_cdc = find("isPcrPrim.tsv", PROJECT_FOLDER)
primer_path_frost = find("isPcrPrim-Frost.tsv", PROJECT_FOLDER)
db = find("emm.fna", PROJECT_FOLDER)

test_sequence_path = find("contig.fasta", __file__)
test_empty_path = find("empty.fasta", __file__)
test_pcr_product_path = find("amplicon.fasta", __file__)

test_blast_product = find("blast.fa.tsv", __file__)

# For ResultRow
string = "SP3LAU\t_emm_89.0\t100\t180\t0\t0\t737626\t737805\t1\t180\t1.93e-89\t333\t180"
string_str = "_emm_89.0"
string_not100 = (
    "SP3LAU\t_emm_89.0\t99\t180\t1\t1\t737626\t737805\t1\t180\t1.93e-89\t333\t180"
)
string_not100_str = "_emm_89.0~"
string_imp = (
    "SP3LAU\t_emm_202.0\t100\t180\t0\t0\t737626\t737805\t1\t180\t1.93e-89\t333\t180"
)
string_imp_str = "_emm_202.0"
string_long = (
    "SP3LAU\t65\t_emm_89.0\t100\t180\t0\t0\t737626\t737805\t1\t180\t1.93e-89\t333\t180"
)

# For BLAST and isPcr
blast_command = 'blastn -db {} -query {} -dust no -perc_identity 95 -culling_limit 1 -outfmt "6 std slen"'.format(
    '"\\"' + db + '"\\"', shlex.quote(test_sequence_path)
)
blast_command_h = 'blastn -db {} -query {} -dust no -perc_identity 100 -culling_limit 1 -outfmt "6 std slen"'.format(
    '"\\"' + db + '"\\"', shlex.quote(test_sequence_path)
)
isPcr_command_cdc = "isPcr {} {} stdout -minPerfect=15 -minGood=15 -maxSize=4000".format(
    shlex.quote(test_sequence_path), shlex.quote(primer_path_cdc)
)
isPcr_command_e_cdc = "isPcr {} {} stdout -minPerfect=20 -minGood=30 -maxSize=4000".format(
    shlex.quote(test_empty_path), shlex.quote(primer_path_cdc)
)

isPcr_command_frost = "isPcr {} {} stdout -minPerfect=15 -minGood=15 -maxSize=4000".format(
    shlex.quote(test_sequence_path), shlex.quote(primer_path_frost)
)
isPcr_command_e_frost = "isPcr {} {} stdout -minPerfect=20 -minGood=30 -maxSize=4000".format(
    shlex.quote(test_empty_path), shlex.quote(primer_path_frost)
)


header = "Query\tBlastHit\tIdentity\tAlignmentLength\tMismatch\tGapOpen\tQueryStart\tQueryEnd\tHitStart\tHitEnd\tE-Value\tBitScore\tSubjectLength\n"

blast_result = (
    "contig1\tEMM1.0\t100.000\t180\t0\t0\t113816\t113995\t1\t180\t1.50e-90\t333\t180"
)
isPcr_result_cdc = ">contig1:113750+114924 emm 1175bp TATTCGCTTAGAAAATTAA GCAAGTTCTTCAGCTTGTTT\nTATTCGCTTAGAAAATTAAaaacaggaacggcttcagtagcggtagcttt\ngactgttttaggggcaggttttgcgaatcaaacagaggttaaggctaacg\ngtgatggtaatcctagggaagttatagaagatcttgcagcaaacaatccc\ngcaatacaaaatatacgtttacgtcacgaaaacaaggacttaaaagcgag\nattagagaatgcaatggaagttgcaggaagagattttaagagagctgaag\naacttgaaaaagcaaaacaagccttagaagaccagcgtaaagatttagaa\nactaaattaaaagaactacaacaagactatgacttagcaaaggaatcaac\naagttgggatagacaaagacttgaaaaagagttagaagagaaaaaggaag\nctcttgaattagcgatagaccaggcaagtcgggactaccatagagctacc\ngctttagaaaaagagttagaagagaaaaagaaagctcttgaattagcgat\nagaccaagcgagtcaggactataatagagctaacgtcttagaaaaagagt\ntagaaacgattactagagaacaagagattaatcgtaatcttttaggcaat\ngcaaaacttgaacttgatcaactttcatctgaaaaagagcagctaacgat\ncgaaaaagcaaaacttgaggaagaaaaacaaatctcagacgcaagtcgtc\naaagccttcgtcgtgacttggacgcatcacgtgaagctaagaaacaggtt\ngaaaaagatttagcaaacttgactgctgaacttgataaggttaaagaaga\ncaaacaaatctcagacgcaagccgtcaaggccttcgccgtgacttggacg\ncatcacgtgaagctaagaaacaggttgaaaaagatttagcaaacttgact\ngctgaacttgataaggttaaagaagaaaaacaaatctcagacgcaagccg\ntcaaggccttcgccgtgacttggacgcatcacgtgaagctaagaaacaag\nttgaaaaagctttagaagaagcaaacagcaaattagctgctcttgaaaaa\ncttaacaaagagcttgaagaaagcaagaaattaacagaaaaagaaaaagc\ntgaactacaagcaaaacttgaagcagaagcaaaagcactcaaagaacaat\ntagcgAAACAAGCTGAAGAACTcGC"
isPcr_result_frost = ">contig1:113750+114820 emm 1071bp TATTCGCTTAGAAAATTAA TTCTTCAAGCTCTTTGTT\nTATTCGCTTAGAAAATTAAaaacaggaacggcttcagtagcggtagcttt\ngactgttttaggggcaggttttgcgaatcaaacagaggttaaggctaacg\ngtgatggtaatcctagggaagttatagaagatcttgcagcaaacaatccc\ngcaatacaaaatatacgtttacgtcacgaaaacaaggacttaaaagcgag\nattagagaatgcaatggaagttgcaggaagagattttaagagagctgaag\naacttgaaaaagcaaaacaagccttagaagaccagcgtaaagatttagaa\nactaaattaaaagaactacaacaagactatgacttagcaaaggaatcaac\naagttgggatagacaaagacttgaaaaagagttagaagagaaaaaggaag\nctcttgaattagcgatagaccaggcaagtcgggactaccatagagctacc\ngctttagaaaaagagttagaagagaaaaagaaagctcttgaattagcgat\nagaccaagcgagtcaggactataatagagctaacgtcttagaaaaagagt\ntagaaacgattactagagaacaagagattaatcgtaatcttttaggcaat\ngcaaaacttgaacttgatcaactttcatctgaaaaagagcagctaacgat\ncgaaaaagcaaaacttgaggaagaaaaacaaatctcagacgcaagtcgtc\naaagccttcgtcgtgacttggacgcatcacgtgaagctaagaaacaggtt\ngaaaaagatttagcaaacttgactgctgaacttgataaggttaaagaaga\ncaaacaaatctcagacgcaagccgtcaaggccttcgccgtgacttggacg\ncatcacgtgaagctaagaaacaggttgaaaaagatttagcaaacttgact\ngctgaacttgataaggttaaagaagaaaaacaaatctcagacgcaagccg\ntcaaggccttcgccgtgacttggacgcatcacgtgaagctaagaaacaag\nttgaaaaagctttagaagaagcaaacagcaaattagctgctcttgaaaaa\ncttAACAAAGAGCTTGAAGAA"
isPcr_result_e = ""


# For Clusterer
header_short = "Isolate\tNumberOfClusters\tAnswers\tSuspectImposters\tAnswersClusters\n"
header_verbose = "Isolate\tNumberOfHits\tNumberOfClusters\tAnswers\tAnswerPositions\tSuspectImposters\tSuspectPositions\tAnswersClusters\n"

clusterer_repr_short = "Clusterer for {} with clustering distance 800bp\nshort output to stdout".format(
    test_blast_product
)
clusterer_result_short = "{}\t2\t_emm_65.0\t_emm_156.0~*\tE6".format(test_blast_product)
clusterer_repr_verbose = "Clusterer for {} with clustering distance 800bp\nverbose output to stdout".format(
    test_blast_product
)
clusterer_result_verbose = "{}{}\t6\t2\t_emm_65.0\t.blast.5:82168\t_emm_156.0~*\t.blast.5:80776\tE6".format(
    header_verbose, test_blast_product
)
