import re

pattern = r"[A-z]+eoffrey"
text = '''The siege of Guînes took place from May to July 1352 when a French army under Geoffrey Zeoffrey de Charny unsuccessfully attempted to recapture the French castle (pictured) at Guînes which had been seized by the English the previous January. The siege was part of the Hundred Years' War and took place during the uneasy and ill-kept truce of Calais. The strongly fortified castle had been taken by the English during a period of nominal truce and the English king, Edward III, decided to keep it. Charny led 4,500 men and retook the town but was unable to either recapture or blockade the castle. After two months of fierce fighting, a large English night attack on the French camp inflicted a heavy defeat and the French withdrew. Guînes was incorporated into the Pale of Calais. The threat posed by this enclave caused the French to garrison 60 fortified positions around it, at ruinous expense. The castle was besieged by the French in 1436 and 1514, but was relieved each time, before falling to the French in 1558.'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    print(match.span())
    print(type(match.span()))
    print(text[match.span()[0]: match.span()[1]])