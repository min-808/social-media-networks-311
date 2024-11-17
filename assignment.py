import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize the graph
social_network = nx.DiGraph()

def add_user(user_name, attributes=None):
    """
    Add a user to the social network.
    """
    if attributes is None:
        attributes = {}
    social_network.add_node(user_name, 
                            attributes=attributes, 
                            posts=[], 
                            seen_posts=[], 
                            comments=[])

def add_connection(from_user, to_user, connection_type):
    """
    Add a directional connection between two users.
    """
    if not social_network.has_edge(from_user, to_user):
        social_network.add_edge(from_user, to_user, connection_types=[])
    social_network[from_user][to_user]['connection_types'].append(connection_type)

def create_post(user_name, content):
    """
    Create a post for a user.
    """
    post = {
        "content": content,
        "creation_time": datetime.now(),
        "comments": [],
        "views": []
    }
    social_network.nodes[user_name]['posts'].append(post)
    return post

def view_post(user_name, post):
    """
    Record that a user has viewed a post.
    """
    if post not in social_network.nodes[user_name]['seen_posts']:
        social_network.nodes[user_name]['seen_posts'].append(post)
    post['views'].append({"user": user_name, "view_time": datetime.now()})

def comment_on_post(user_name, post, content):
    """
    Add a comment to a post by a user.
    """
    comment = {
        "user": user_name,
        "content": content,
        "creation_time": datetime.now()
    }
    post['comments'].append(comment)
    social_network.nodes[user_name]['comments'].append(comment)

def draw_social_network():
    """
    Draw the social network graph using matplotlib.
    """
    plt.figure(figsize=(12, 8))
    
    # Node positions
    pos = nx.spring_layout(social_network)
    
    # Draw nodes and edges
    nx.draw_networkx_nodes(social_network, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(social_network, pos, arrowstyle="->", arrowsize=15, edge_color='gray')
    
    # Node labels
    node_labels = {node: node for node in social_network.nodes()}
    nx.draw_networkx_labels(social_network, pos, labels=node_labels, font_size=12, font_color='black')
    
    # Edge labels (connection types)
    edge_labels = {
        (u, v): ", ".join(data['connection_types']) 
        for u, v, data in social_network.edges(data=True)
    }
    nx.draw_networkx_edge_labels(social_network, pos, edge_labels=edge_labels, font_size=10)
    
    # Display the graph
    plt.title("Social Network Graph")
    plt.axis("off")
    plt.show()

# Example usage
if __name__ == "__main__":
    # Add users
    add_user("alice", {"real_name": "Alice Smith", "age": 30, "location": "NYC"})
    add_user("bob", {"real_name": "Bob Jones", "age": 25, "location": "LA"})
    add_user("carol", {"real_name": "Carol White", "age": 35, "location": "Chicago"})

    # Add connections
    add_connection("alice", "bob", "follows")
    add_connection("bob", "alice", "friends")
    add_connection("alice", "carol", "co-worker")

    # Alice creates a post
    post1 = create_post("alice", "Hello, world!")

    # Bob views Alice's post
    view_post("bob", post1)

    # Bob comments on Alice's post
    comment_on_post("bob", post1, "Nice post!")

    # Draw the social network graph
    draw_social_network()