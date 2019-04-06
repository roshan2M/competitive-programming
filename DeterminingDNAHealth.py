def binarySearch(array, first, last, value):
    middle = first + (last - first)//2
    if array[first][0] == value:
        return first
    elif array[middle][0] == value:
        return middle
    elif array[last][0] == value:
        return last
    elif array[middle][0] > value:
        last = middle
    else:
        first = middle
    if last - first <= 1:
        if array[last][0] < value:
            return last
        return first
    return binarySearch(array, first, last, value)

class Node:
    def __init__(self, id):
        self.id = id
        self.nodes = {}
        self.outputs = []

    def addWord(self, s, index, value):
        """
        Recursively adds string final to the graph, associated to given value.
        
        Removes one letter at a time from s until an empty string is reached.
        
        Then maps the index (unique) to the associated value.
        """
        if len(s) == 0:
            length = len(self.outputs)
            previous = 0 if length == 0 else self.outputs[length-1][1]
            self.outputs.append((index, previous + value)) # Index will be unique
            return
        first = s[0]
        if first not in self.nodes:
            self.nodes[first] = Node(first)
        self.nodes[first].addWord(s[1:], index, value)
    
    def getNodeValue(self, start, end):
        """
        Returns the value of the outputs based on the start and end accepted indexes of the word.
        """
        outputLen = len(self.outputs)
        if outputLen == 0:
            return 0
        startIdx = binarySearch(self.outputs, 0, outputLen-1, start-1)
        endIdx = binarySearch(self.outputs, 0, outputLen-1, end)

        value = 0
        if self.outputs[startIdx][0] < start:
            value -= self.outputs[startIdx][1]
        if self.outputs[endIdx][0] <= end:
            value += self.outputs[endIdx][1]
        return value

    def getWordValue(self, s, start, end):
        """
        Gets all substrings of s with an associated healthy value in the automaton.

        Returns the total value of all such substrings.
        """
        totalValue = 0
        length = len(s)
        for i in range(length):
            currentNode = self
            index = i
            
            while index < length:
                if s[index] not in currentNode.nodes:
                    break
                currentNode = currentNode.nodes[s[index]]
                value = currentNode.getNodeValue(start, end)
                totalValue += value
                index += 1
        return totalValue

    def prettyPrint(self, prefix):
        """
        Outputs a readable format of the node and all its children.
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

if __name__ == '__main__':
    n = int(raw_input())

    genes = raw_input().rstrip().split()
    health = map(int, raw_input().rstrip().split())
    dnaGraph = buildDnaTrie(genes, health)

    s = int(raw_input())

    minHealth, maxHealth = None, None
    for s_itr in xrange(s):
        firstLastd = raw_input().split()

        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]

        health = dnaGraph.getWordValue(d, first, last)
        minHealth = health if minHealth is None else min(minHealth, health)
        maxHealth = health if maxHealth is None else max(maxHealth, health)

    print minHealth, maxHealth
