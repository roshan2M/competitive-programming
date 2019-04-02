class Node:
    def __init__(self, id):
        self.id = id
        self.outputs = {}
        self.nodes = {}
        self.fail = None

    def addWord(self, s, index, value):
        """
        Recursively adds string final to the graph, associated to given value.
        
        Removes one letter at a time from s until an empty string is reached.
        
        Then maps the index (unique) to the associated value.
        """
        if len(s) == 0:
            self.outputs[index] = value # Index must be unique
            return
        first = s[0]
        if first not in self.nodes:
            self.nodes[first] = Node(first)
        self.nodes[first].addWord(s[1:], index, value)

    def getWordValue(self, s, start, end):
        """
        Gets all substrings of s with an associated value in the trie.

        Returns the total value of all such substrings.
        """
        totalValue = 0
        currentNode = self
        for c in s:
            while c not in currentNode.nodes and currentNode.fail:
                currentNode = currentNode.fail
            if c in currentNode.nodes:
                currentNode = currentNode.nodes[c]
                for key, value in currentNode.outputs.iteritems():
                    if key >= start and key <= end:
                        totalValue += value
        return totalValue

    def prettyPrint(self, prefix):
        """
        Outputs a readable format of the node.
        """
        print(prefix + 'Id: ' + (self.id if self.id else 'None'))
        print(prefix + 'Fail: ' + (self.fail.id if self.fail and self.fail.id else 'None'))
        print(prefix + 'Outputs: ' + str(self.outputs))
        for key, node in self.nodes.iteritems():
            node.prettyPrint(prefix + '\t')

def buildDnaTrie(genes, health):
    startNode = Node(None)
    for i in range(len(genes)):
        startNode.addWord(genes[i], i, health[i])
    return startNode

def buildDnaFails(start):
    queue = []
    for node in start.nodes.values():
        node.fail = start
        queue.append(node)

    while queue:
        current = queue.pop(0)
        fail = current.fail
        for cKey, cNode in current.nodes.iteritems():
            while not cNode.fail:
                for key, node in fail.nodes.iteritems():
                    if key == cKey:
                        cNode.fail = node
                        cNode.outputs = mergeTwoDicts(cNode.outputs, node.outputs)
                if not cNode.fail:
                    if not fail.fail:
                        cNode.fail = start
                    else:
                        fail = fail.fail
            queue.append(cNode)

def mergeTwoDicts(x, y):
    z = x.copy()
    z.update(y)
    return z

if __name__ == '__main__':
    n = int(raw_input())

    genes = raw_input().rstrip().split()
    health = map(int, raw_input().rstrip().split())
    dnaGraph = buildDnaTrie(genes, health)
    buildDnaFails(dnaGraph)

    s = int(raw_input())

    results = []
    for s_itr in xrange(s):
        firstLastd = raw_input().split()

        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]

        results.append(dnaGraph.getWordValue(d, first, last))

    print min(results), max(results)
