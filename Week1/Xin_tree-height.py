# python3

import sys, threading
import queue

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

    def addChild(self, child):
        self.children.append(child)

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
            nodes = [Node(i) for i in range(self.n)]
            for i in range(self.n):
                if self.parent[i] == -1:
                    self.root = nodes[i]
                else:
                    nodes[self.parent[i]].addChild(nodes[i])

            #生成一个基本队列q LILO，队列中存放的是树中同一层的 node
            q = queue.Queue()
            #放入root的值到q，从 root 开始一层一层的遍历这棵树，当前是 root 所在的层，所以只有 root 一个 node
            q.put(self.root)
            #初始高度
            height = 0
            while(not q.empty()):
                size = q.qsize()
                if size > 0:
                    height = height + 1
                # 然后把当前层中所有 node 的 children 放入队列，并同时依次排空当前层的 node
                # 也就是说，当前 for 循环之后，这一层的所有 node 都被 get 出来了。
                # 当此 for 循环结束后，也就是下一次 while 循环开始前，队列中就只有下一层 node 了
                for j in range(size):
                    item = q.get()
                    for i in item.children:
                        q.put(i)
            return height
            #也就是说下一次while的时候遍历的是下一层

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
