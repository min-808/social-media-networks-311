import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize the graph
social_network = nx.DiGraph()

def add_user(user_name, attributes = None):
    """ Add a user to the social network. """

    if attributes is None:
        attributes = {}
    social_network.add_node(user_name, 
                            attributes=attributes, 
                            posts=[], 
                            seen_posts=[], 
                            comments=[])

def add_connection(from_user, to_user, connection_type):
    """ Add a directional connection between two users. """
    
    if not social_network.has_edge(from_user, to_user):
        social_network.add_edge(from_user, to_user, connection_types=[])
    social_network[from_user][to_user]['connection_types'].append(connection_type)

def create_post(user_name, content):
    """ Create a post for a user. """

    post = {
        "content": content,
        "creation_time": datetime.now(),
        "comments": [],
        "views": []
    }
    social_network.nodes[user_name]['posts'].append(post)
    return post

def view_post(user_name, post):
    """ Record that a user has viewed a post. """

    if post not in social_network.nodes[user_name]['seen_posts']:
        social_network.nodes[user_name]['seen_posts'].append(post)
    post['views'].append({"user": user_name, "view_time": datetime.now()})

def comment_on_post(user_name, post, content):
    """ Add a comment to a post by a user. """
    comment = {
        "user": user_name,
        "content": content,
        "creation_time": datetime.now()
    }
    post['comments'].append(comment)
    social_network.nodes[user_name]['comments'].append(comment)

def draw_social_network():
    """ Draw the social network graph using matplotlib. """
    plt.figure(figsize=(14, 10))
    
    # Node positions
    pos = nx.spring_layout(social_network)
    
    # Draw nodes and edges
    nx.draw_networkx_nodes(social_network, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(social_network, pos, arrowstyle="->", arrowsize=10, edge_color='black')
    
    # Node labels
    node_labels = {node: node for node in social_network.nodes()}
    nx.draw_networkx_labels(social_network, pos, labels=node_labels, font_size=8, font_color='black')
    
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
    add_user("alice", {"real_name": "Alice Smith", "age": 30, "location": "Oahu"})
    add_user("bob", {"real_name": "Bob Jones", "age": 25, "location": "Oahu"})
    add_user("carol", {"real_name": "Carol White", "age": 35, "location": "Oahu"})
    add_user("dave", {"real_name": "Dave Brown", "age": 28, "location": "Maui"})
    add_user("eve", {"real_name": "Eve Davis", "age": 22, "location": "Oahu"})
    add_user("james", {"real_name": "James Smith", "age": 19, "location": "Kauai"})
    add_user("maria", {"real_name": "Maria Garcia", "age": 23, "location": "Oahu"})
    # add_user("william", {"real_name": "William Johnson", "age": 20, "location": "Maui"})
    # add_user("taylor", {"real_name": "Taylor Jackson", "age": 23, "location": "Maui"})

    # Add connections
    add_connection("alice", "eve", "follows")
    add_connection("alice", "taylor", "follows")
    add_connection("alice", "carol", "blocked")

    add_connection("bob", "alice", "follows")
    add_connection("bob", "carol", "follows")

    add_connection("carol", "bob", "follows")
    add_connection("carol", "eve", "follows")

    add_connection("dave", "taylor", "follows")
    add_connection("dave", "bob", "follows")

    add_connection("eve", "alice", "follows")
    add_connection("eve", "bob", "follows")
    add_connection("eve", "taylor", "blocked")

    add_connection("james", "maria", "follows")
    add_connection("james", "taylor", "follows")
    add_connection("james", "bob", "blocked")

    add_connection("maria", "carol", "follows")
    add_connection("maria", "dave", "follows")
    add_connection("maria", "bob", "follows")

    # Alice creates a post
    post1 = create_post("alice", "Hello, world!")

    # Bob views Alice's post
    view_post("bob", post1)
    view_post("alice", post1)
    view_post("maria", post1)

    # Bob comments on Alice's post
    comment_on_post("bob", post1, "Nice post!")

    # Carol creates a post
    post2 = create_post("carol", "Excited about the new project!")

    # Dave views and comments on Carol's post
    view_post("dave", post2)
    comment_on_post("dave", post2, "Looking forward to it!")

    # Eve creates a post
    post3 = create_post("eve", "Just moved to Oahu, loving it here!")

    # Alice and Bob view Eve's post
    view_post("alice", post3)
    view_post("bob", post3)

    # Alice comments on Eve's post
    comment_on_post("alice", post3, "Oahu is amazing!")

    # Draw the social network graph
    draw_social_network()

    # Example operations on the graph:

    # Get all user's posts
    print(f"alice's posts: {social_network.nodes['alice']['posts']}")
    
    # Get all comments under a post
    user_posts = social_network.nodes["alice"]["posts"]
    first_post = user_posts[0]
    comments = first_post["comments"]
    for comment in comments:
      print(f"User: {comment['user']}, Comment: {comment['content']}, Time: {comment['creation_time']}")

    # Get all views of a post
    print(f"User: post1 has {len(post1['views'])} views")

    # Get the follower count of a user
    user_followers = social_network.in_degree("bob")
    print(f"User: bob has {user_followers} followers")