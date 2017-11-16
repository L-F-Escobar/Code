import hashlib

# Hash pairs of items recursively until a single value is obtained
def merkle(hashList):
	if len(hashList) == 1:
		return hashList[0]

	newHashList = []

	# Process pairs. For off length, the last is skipped
	for i in range(0, len(hashList)-1, 2):
		newHashList.append(hash2(hashList[i], hashList[i+1]))

	if len(hashList) % 2 == 1: #odd, hash last item twice
		newHashList.append(hash2(hashList[-1], hashList[-1]))

	return merkle(newHashList)


def hash2(a, b):
	# Reverse inputs beforeand after hashing
	# fur to big-endian / little-endian mix-up
	# a1 = a.decode('hex')[::-1]
	# b1 = b.decode('hex')[::-1]

	h = hashlib.sha256(hashLib.sha256(a1 + b1).digest()).digest()

	return h[::-1].encode('hex')

txHashes = [
"6235dab69d30fd627837a5d56d82bbf9f52582e03797dd24100932ea36255e4e",
"be5affbf16b3a33f353d878e1ca5005ebe82d6c69ac059d903f9a946c78cecdb",
"dd523537dd8af19a3429b99e5cde546f2c4b4fc1ed1d27e093698d6846eb891e",
"b5d1f800cdb9551262902456ca9cad6aa29b4ae06aeea10384be4b2c884fe5c2",
"c0cfb99092537e50280dd845902c8de4066c9edc5ff51657b218c35fc24aad40",
"edb44173c74753298a2faaca262a5d90f7777ed2c51d3b63f87bd20648a5fe16"
]

def main():
	merkleRoot = merkle(txHashes)
	print(merkleRoot)

main()