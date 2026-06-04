import time
class Node:
  def __init__(self, node_id):
    self.node_id = node_id
  def send_message(self, message):
    print(f"Node {self.node_id} send: {message}")

class TokenRingNetwork:
  def __init__(self, nodes):
    self.nodes = nodes
    self.token_position = 0

  def pass_token(self, rounds=1):
    for _ in range(rounds):
      for i in range(len(self.nodes)):
        current_node = self.nodes[self.token_position]
        current_node.send_message(f"Hello from Node{current_node.node_id}")
        time.sleep(1)

        #pass token to next node
        self.token_position = (self.token_position + 1) % len(self.nodes)

nodes = [Node(1), Node(2), Node(3), Node(4)]
network = TokenRingNetwork(nodes)
print("\nStarting Token Ring Simulation...")
network.pass_token(rounds=2)