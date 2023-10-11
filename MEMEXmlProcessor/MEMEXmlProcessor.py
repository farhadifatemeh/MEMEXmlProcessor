
import xml.etree.cElementTree as et

tree = et.parse('MEMEAllPatterns.xml')
root = tree.getroot()
memeMotifs = []

for motif in root.iter('motif'):
    regular_expression = motif.find('regular_expression')
    regular_expressionmotif = " ".join(regular_expression.text.split())
    if len(regular_expressionmotif) > 6:
        print("'", regular_expressionmotif, "',")
        memeMotifs.append(regular_expressionmotif)
print(memeMotifs)
print(len(memeMotifs))