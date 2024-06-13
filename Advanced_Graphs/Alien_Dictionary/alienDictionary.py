class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # We can use topological sort to solve this problem
        # Topological sort involves using a DAG -> Directed Acyclic Graph (Agraph that has directed edges but no cycles)
        # the words dictionary in this problem is already sorted: "wrt", "wrf" ...
        # In this case, "t comes before f"   t->f. w->e
        # w -> e -> r -> t -> f

        # if a cycle exists in our graph where we happen to traverse through the same letter after constructing the order than we need to return "" as the word order is invalid
        # To visit the nodes in order we perform a post-order DFS where we add the last node we visit in DFS into the output string and recursively as we exit from the function calls add the nodes visited
        # We have been so far performing topological sort with adding elements as a Post Order DFS

        # part I am unsure of is building the Adj_list
        adj_list = {c:set() for w in words for c in w} # we map every char to a set to make sure we dont have duplicates

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLength = min(len(w1), len(w2))
            # if the first word is longer and has the same prefix as the second word then the words list is invalid
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return False
            # If not we want to go through every character in the shorter word length and 
            # only extract the different character from them
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
                
        visited = {} # False = visited, True = current path
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            # add the c to the path
            visited[c] = True
            for nei in adj_list[c]:
                if dfs(nei): # We detected a loop and we can return immediately
                    return True
            # mark the node as visited but out of current Path
            visited[c] = False
            res.append(c)

        for c in adj_list:
            if dfs(c):
                return ""
        return "".join(res[::-1])