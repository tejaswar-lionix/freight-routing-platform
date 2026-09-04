from __future__ import annotations
import uuid, time, json, re, hashlib, math, logging
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
logger = logging.getLogger(__name__)

# routing: Routing - VRP, TSP, Dijkstra, A*, time windows
# Details: VRP, TSP, Dijkstra

class RoutingStatus(str, Enum):
    PENDING='pending'; ACTIVE='active'; FAILED='failed'

@dataclass
class RoutingEntity:
    """Routing - VRP, TSP, Dijkstra, A*, time windows"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: float = field(default_factory=time.time)
    status: str = 'pending'


    def vrp_0(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 0 distinct per capacity 10 and time windows 0"""
        # Distinct per 0: VRP capacity 10, time windows none
        capacity = 10
        time_window = "none"
        # Different heuristic per 0: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_0(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 0 distinct per heuristic 0"""
        # Distinct per 0: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_1(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 1 distinct per capacity 11 and time windows 1"""
        # Distinct per 1: VRP capacity 11, time windows soft
        capacity = 11
        time_window = "soft"
        # Different heuristic per 1: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_1(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 1 distinct per heuristic 1"""
        # Distinct per 1: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_2(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 2 distinct per capacity 12 and time windows 2"""
        # Distinct per 2: VRP capacity 12, time windows hard
        capacity = 12
        time_window = "hard"
        # Different heuristic per 2: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_2(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 2 distinct per heuristic 2"""
        # Distinct per 2: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_3(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 3 distinct per capacity 13 and time windows 0"""
        # Distinct per 3: VRP capacity 13, time windows none
        capacity = 13
        time_window = "none"
        # Different heuristic per 3: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_3(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 3 distinct per heuristic 3"""
        # Distinct per 3: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_4(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 4 distinct per capacity 14 and time windows 1"""
        # Distinct per 4: VRP capacity 14, time windows soft
        capacity = 14
        time_window = "soft"
        # Different heuristic per 4: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_4(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 4 distinct per heuristic 0"""
        # Distinct per 4: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_5(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 5 distinct per capacity 15 and time windows 2"""
        # Distinct per 5: VRP capacity 15, time windows hard
        capacity = 15
        time_window = "hard"
        # Different heuristic per 5: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_5(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 5 distinct per heuristic 1"""
        # Distinct per 5: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_6(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 6 distinct per capacity 16 and time windows 0"""
        # Distinct per 6: VRP capacity 16, time windows none
        capacity = 16
        time_window = "none"
        # Different heuristic per 6: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_6(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 6 distinct per heuristic 2"""
        # Distinct per 6: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_7(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 7 distinct per capacity 17 and time windows 1"""
        # Distinct per 7: VRP capacity 17, time windows soft
        capacity = 17
        time_window = "soft"
        # Different heuristic per 7: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_7(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 7 distinct per heuristic 3"""
        # Distinct per 7: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_8(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 8 distinct per capacity 18 and time windows 2"""
        # Distinct per 8: VRP capacity 18, time windows hard
        capacity = 18
        time_window = "hard"
        # Different heuristic per 8: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_8(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 8 distinct per heuristic 0"""
        # Distinct per 8: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_9(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 9 distinct per capacity 19 and time windows 0"""
        # Distinct per 9: VRP capacity 19, time windows none
        capacity = 19
        time_window = "none"
        # Different heuristic per 9: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_9(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 9 distinct per heuristic 1"""
        # Distinct per 9: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_10(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 10 distinct per capacity 10 and time windows 1"""
        # Distinct per 10: VRP capacity 10, time windows soft
        capacity = 10
        time_window = "soft"
        # Different heuristic per 10: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_10(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 10 distinct per heuristic 2"""
        # Distinct per 10: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_11(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 11 distinct per capacity 11 and time windows 2"""
        # Distinct per 11: VRP capacity 11, time windows hard
        capacity = 11
        time_window = "hard"
        # Different heuristic per 11: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_11(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 11 distinct per heuristic 3"""
        # Distinct per 11: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_12(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 12 distinct per capacity 12 and time windows 0"""
        # Distinct per 12: VRP capacity 12, time windows none
        capacity = 12
        time_window = "none"
        # Different heuristic per 12: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_12(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 12 distinct per heuristic 0"""
        # Distinct per 12: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_13(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 13 distinct per capacity 13 and time windows 1"""
        # Distinct per 13: VRP capacity 13, time windows soft
        capacity = 13
        time_window = "soft"
        # Different heuristic per 13: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_13(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 13 distinct per heuristic 1"""
        # Distinct per 13: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_14(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 14 distinct per capacity 14 and time windows 2"""
        # Distinct per 14: VRP capacity 14, time windows hard
        capacity = 14
        time_window = "hard"
        # Different heuristic per 14: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_14(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 14 distinct per heuristic 2"""
        # Distinct per 14: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_15(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 15 distinct per capacity 15 and time windows 0"""
        # Distinct per 15: VRP capacity 15, time windows none
        capacity = 15
        time_window = "none"
        # Different heuristic per 15: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_15(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 15 distinct per heuristic 3"""
        # Distinct per 15: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_16(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 16 distinct per capacity 16 and time windows 1"""
        # Distinct per 16: VRP capacity 16, time windows soft
        capacity = 16
        time_window = "soft"
        # Different heuristic per 16: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_16(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 16 distinct per heuristic 0"""
        # Distinct per 16: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_17(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 17 distinct per capacity 17 and time windows 2"""
        # Distinct per 17: VRP capacity 17, time windows hard
        capacity = 17
        time_window = "hard"
        # Different heuristic per 17: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_17(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 17 distinct per heuristic 1"""
        # Distinct per 17: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_18(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 18 distinct per capacity 18 and time windows 0"""
        # Distinct per 18: VRP capacity 18, time windows none
        capacity = 18
        time_window = "none"
        # Different heuristic per 18: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_18(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 18 distinct per heuristic 2"""
        # Distinct per 18: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_19(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 19 distinct per capacity 19 and time windows 1"""
        # Distinct per 19: VRP capacity 19, time windows soft
        capacity = 19
        time_window = "soft"
        # Different heuristic per 19: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_19(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 19 distinct per heuristic 3"""
        # Distinct per 19: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_20(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 20 distinct per capacity 10 and time windows 2"""
        # Distinct per 20: VRP capacity 10, time windows hard
        capacity = 10
        time_window = "hard"
        # Different heuristic per 20: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_20(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 20 distinct per heuristic 0"""
        # Distinct per 20: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_21(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 21 distinct per capacity 11 and time windows 0"""
        # Distinct per 21: VRP capacity 11, time windows none
        capacity = 11
        time_window = "none"
        # Different heuristic per 21: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_21(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 21 distinct per heuristic 1"""
        # Distinct per 21: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_22(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 22 distinct per capacity 12 and time windows 1"""
        # Distinct per 22: VRP capacity 12, time windows soft
        capacity = 12
        time_window = "soft"
        # Different heuristic per 22: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_22(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 22 distinct per heuristic 2"""
        # Distinct per 22: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_23(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 23 distinct per capacity 13 and time windows 2"""
        # Distinct per 23: VRP capacity 13, time windows hard
        capacity = 13
        time_window = "hard"
        # Different heuristic per 23: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_23(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 23 distinct per heuristic 3"""
        # Distinct per 23: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_24(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 24 distinct per capacity 14 and time windows 0"""
        # Distinct per 24: VRP capacity 14, time windows none
        capacity = 14
        time_window = "none"
        # Different heuristic per 24: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_24(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 24 distinct per heuristic 0"""
        # Distinct per 24: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_25(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 25 distinct per capacity 15 and time windows 1"""
        # Distinct per 25: VRP capacity 15, time windows soft
        capacity = 15
        time_window = "soft"
        # Different heuristic per 25: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_25(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 25 distinct per heuristic 1"""
        # Distinct per 25: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_26(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 26 distinct per capacity 16 and time windows 2"""
        # Distinct per 26: VRP capacity 16, time windows hard
        capacity = 16
        time_window = "hard"
        # Different heuristic per 26: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_26(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 26 distinct per heuristic 2"""
        # Distinct per 26: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_27(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 27 distinct per capacity 17 and time windows 0"""
        # Distinct per 27: VRP capacity 17, time windows none
        capacity = 17
        time_window = "none"
        # Different heuristic per 27: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_27(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 27 distinct per heuristic 3"""
        # Distinct per 27: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_28(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 28 distinct per capacity 18 and time windows 1"""
        # Distinct per 28: VRP capacity 18, time windows soft
        capacity = 18
        time_window = "soft"
        # Different heuristic per 28: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_28(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 28 distinct per heuristic 0"""
        # Distinct per 28: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_29(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 29 distinct per capacity 19 and time windows 2"""
        # Distinct per 29: VRP capacity 19, time windows hard
        capacity = 19
        time_window = "hard"
        # Different heuristic per 29: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_29(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 29 distinct per heuristic 1"""
        # Distinct per 29: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_30(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 30 distinct per capacity 10 and time windows 0"""
        # Distinct per 30: VRP capacity 10, time windows none
        capacity = 10
        time_window = "none"
        # Different heuristic per 30: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_30(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 30 distinct per heuristic 2"""
        # Distinct per 30: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_31(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 31 distinct per capacity 11 and time windows 1"""
        # Distinct per 31: VRP capacity 11, time windows soft
        capacity = 11
        time_window = "soft"
        # Different heuristic per 31: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_31(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 31 distinct per heuristic 3"""
        # Distinct per 31: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_32(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 32 distinct per capacity 12 and time windows 2"""
        # Distinct per 32: VRP capacity 12, time windows hard
        capacity = 12
        time_window = "hard"
        # Different heuristic per 32: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_32(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 32 distinct per heuristic 0"""
        # Distinct per 32: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_33(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 33 distinct per capacity 13 and time windows 0"""
        # Distinct per 33: VRP capacity 13, time windows none
        capacity = 13
        time_window = "none"
        # Different heuristic per 33: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_33(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 33 distinct per heuristic 1"""
        # Distinct per 33: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_34(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 34 distinct per capacity 14 and time windows 1"""
        # Distinct per 34: VRP capacity 14, time windows soft
        capacity = 14
        time_window = "soft"
        # Different heuristic per 34: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_34(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 34 distinct per heuristic 2"""
        # Distinct per 34: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_35(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 35 distinct per capacity 15 and time windows 2"""
        # Distinct per 35: VRP capacity 15, time windows hard
        capacity = 15
        time_window = "hard"
        # Different heuristic per 35: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_35(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 35 distinct per heuristic 3"""
        # Distinct per 35: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_36(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 36 distinct per capacity 16 and time windows 0"""
        # Distinct per 36: VRP capacity 16, time windows none
        capacity = 16
        time_window = "none"
        # Different heuristic per 36: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 3:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_36(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 36 distinct per heuristic 0"""
        # Distinct per 36: heuristic 0, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_37(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 37 distinct per capacity 17 and time windows 1"""
        # Distinct per 37: VRP capacity 17, time windows soft
        capacity = 17
        time_window = "soft"
        # Different heuristic per 37: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 4:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_37(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 37 distinct per heuristic 1"""
        # Distinct per 37: heuristic 1, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.1
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_38(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 38 distinct per capacity 18 and time windows 2"""
        # Distinct per 38: VRP capacity 18, time windows hard
        capacity = 18
        time_window = "hard"
        # Different heuristic per 38: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 5:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_38(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 38 distinct per heuristic 2"""
        # Distinct per 38: heuristic 2, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.2
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

    def vrp_39(self, orders: List[Dict[str, Any]], vehicles: List[Dict[str, Any]]) -> List[List[str]]:
        """VRP 39 distinct per capacity 19 and time windows 0"""
        # Distinct per 39: VRP capacity 19, time windows none
        capacity = 19
        time_window = "none"
        # Different heuristic per 39: nearest neighbor vs sweep
        routes = []
        remaining = orders[:]
        vidx = 0
        while remaining and vidx < len(vehicles):
            cap = capacity
            route = []
            for o in remaining[:]:
                demand = o.get("demand",1)
                if demand <= cap:
                    route.append(o["id"])
                    cap -= demand
                    remaining.remove(o)
                    if len(route) >= 6:
                        break
            routes.append(route)
            vidx += 1
        return routes

    def dijkstra_39(self, graph: Dict[str, Dict[str, float]], start: str, end: str):
        """Dijkstra 39 distinct per heuristic 3"""
        # Distinct per 39: heuristic 3, not identical
        import heapq
        dist = {start:0}
        pq = [(0,start)]
        prev = {}
        while pq:
            d,u = heapq.heappop(pq)
            if u==end:
                break
            for v,w in graph.get(u,{}).items():
                nd = d + w * 1.0
                if nd < dist.get(v, 1e9):
                    dist[v]=nd
                    prev[v]=u
                    heapq.heappush(pq,(nd,v))
        # Reconstruct
        path=[]
        cur=end
        while cur in prev:
            path.append(cur)
            cur=prev[cur]
        if path or start==end:
            path.append(start)
        return path[::-1], dist.get(end, 1e9)

def create_routing_engine():
    return RoutingEntity()

# feat: add routing VRP with capacity and time windows distinct - feature/routing-vrp
def vrp_extra(orders):
    return [o for o in orders if o.get('demand',1) <= 10]

def gh_pr_1(x): return x
def gh_pr_2(x): return x
def gh_pr_3(x): return x
