from pq import PriorityQueue, Graph, Vertex


# 最短路径
# G - 无向赋权图
# start - 开始节点
# 返回从开始节点到其它所有节点的最短带权路径
def dijkstra(G, start):
    pq = PriorityQueue()  # 创建优先队列
    start.setDistance(0)  # 起点距离设置为0，其它节点距离默认maxsize
    # 将节点排入优先队列，start在最前面
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        # 取从start开始距离最小的节点出队列，作为当前节点
        # 当前节点已解出最短路径
        currentVert = pq.delMin()
        # 遍历节点的所有邻接节点
        for nextVert in currentVert.getConnections():
            # 从当前节点出发，逐个加上邻接节点的距离进行检验
            newDist = currentVert.getDistance() \
                      + currentVert.getWeight(nextVert)
            # 如果小于邻接节点原有距离，就更新邻接节点
            if newDist < nextVert.getDistance():
                # 更新距离值
                nextVert.setDistance(newDist)
                # 更新返回路径
                nextVert.setPred(currentVert)
                # 更新优先队列
                pq.decreaseKey(nextVert, newDist)


G = Graph()
ndedge = [('u', 'v', 2), ('u', 'w', 5), ('u', 'x', 1),
          ('v', 'x', 2), ('v', 'w', 3), ('x', 'w', 3),
          ('x', 'y', 1), ('w', 'y', 1), ('w', 'z', 5),
          ('y', 'z', 1)]
for nd in ndedge:
    G.addEdge(nd[0], nd[1], nd[2])
    G.addEdge(nd[1], nd[0], nd[2])
start = G.getVertex('u')
dijkstra(G, start)
print(G)
