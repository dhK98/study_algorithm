# 실패 코드 
# 이진 트리를 배열로 만들려고 하였으나, 올바르게 생성되지 않음 
import sys
sys.setrecursionlimit(10000000)   

def solution(nodeinfo):
    answer = []
    # 좌표로 이진 트리를 구성 후 전위 순회, 후위 순회
    bianry_tree = get_bianry_tree(nodeinfo)
    pre_arr = []
    search_pre_node(bianry_tree,pre_arr,0)
    answer.append(pre_arr)
    after_arr = []
    search_after_node(bianry_tree,after_arr,0)
    answer.append(after_arr)
    print(bianry_tree)
    return answer

def get_bianry_tree(nodeinfo):
    nodeinfo = [[x,y,idx+1]for idx,(x,y) in enumerate(nodeinfo)]
    sorted_node = sorted(nodeinfo, key = lambda x : (x[1],-x[0]), reverse = True)
    return [node_info[2] for node_info in sorted_node]

def search_pre_node(binary_tree, arr, idx):
    if idx >= len(binary_tree):
        return
    arr.append(binary_tree[idx])
    search_pre_node(binary_tree, arr, idx * 2 + 1)
    search_pre_node(binary_tree, arr, idx * 2 + 2)
    return

def search_after_node(binary_tree, arr, idx):
    if idx >= len(binary_tree):
        return
    search_after_node(binary_tree, arr, idx * 2 + 1)
    search_after_node(binary_tree, arr, idx * 2 + 2)
    arr.append(binary_tree[idx])
    return

# 이진 트릭 구현으로 성공
import sys
sys.setrecursionlimit(100000000)

# 노드 클래스를 생성
class node:
    def __init__(self, info):
        # 원본 인덱스(식별 지표)
        self.number = info[2]
        # 좌표
        self.data = info[:2]
        self.right = None
        self.left = None
        
    # 노드를 추가하는 함수를 생성
def addnode(root, info):
    if info[0] > root.data[0]:
        if not root.right: root.right = node(info)
        else: addnode(root.right,info)
    elif  info[0] < root.data[0]:
        if not root.left: root.left = node(info)
        else: addnode(root.left,info)
    # 전위 후위 탐색 함수
def preorder(root, order):
    if root != None:
        order.append(root.number)
        preorder(root.left, order)
        preorder(root.right, order)
    
def afterorder(root, order):
    if root != None:
        afterorder(root.left, order)
        afterorder(root.right, order)
        order.append(root.number)

def solution(nodeinfo):
    nodeinfo = [[x,y,idx + 1] for idx,(x,y) in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key = lambda x: x[1], reverse = True)
    root = node(nodeinfo[0])
    # 추가
    for info in nodeinfo[1:]:
        addnode(root,info)
    # 조회
    preorderList = []
    preorder(root,preorderList)
    
    afterorderList = []
    afterorder(root,afterorderList)
       
    return [preorderList,afterorderList]

