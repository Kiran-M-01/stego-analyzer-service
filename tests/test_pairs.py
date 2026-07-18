from analyzer.pairs import PairGenerator

pairs = PairGenerator.generate()

print("Total pairs:", len(pairs))

print("\nFirst 10 pairs:")

for pair in pairs[:10]:
    print(pair)

print("\nLast 5 pairs:")

for pair in pairs[-5:]:
    print(pair)