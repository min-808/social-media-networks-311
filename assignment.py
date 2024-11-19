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
    plt.figure(figsize=(16, 10))
    
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

def compute_post_importance(post, criteria="comments"):
    """Compute the importance of a post based on the given criteria."""
    if criteria == "comments":
        return len(post["comments"])
    elif criteria == "views":
        return len(post["views"])
    elif criteria == "blend":
        return len(post["comments"]) + 0.5 * len(post["views"])
    else:
        raise ValueError("Invalid importance criteria.")
    
def draw_network(criteria="comments"):
    """Draw a diagram of the social media network showing authorship and viewership edges, with important posts highlighted."""
    plt.figure(figsize=(12, 8))
    graph = nx.DiGraph()

    # Add users and posts as nodes
    for user_name in social_network.nodes:
        graph.add_node(user_name, node_type="user")
        for post in social_network.nodes[user_name]["posts"]:
            graph.add_node(id(post), node_type="post", importance=compute_post_importance(post, criteria))

            # Add edges: user → post (authorship)
            graph.add_edge(user_name, id(post), edge_type="authorship")

            # Add edges: user → post (viewership)
            for view in post["views"]:
                graph.add_edge(view["user"], id(post), edge_type="viewership")

    # Compute importance and highlight important posts
    node_colors = []
    node_sizes = []
    for node in graph.nodes(data=True):
        if node[1].get("node_type") == "post":
            importance = node[1].get("importance", 0)
            print(f"importance of {node}: {importance}")
            if importance >= 7:  # Threshold for "important"
                node_colors.append("red")  # Highly important
            elif importance >= 5:
                node_colors.append("orange")  # Less important
            else:
                node_colors.append("green")
            node_sizes.append(200 + importance * 10)  # Scale size by importance
        else:
            node_colors.append("lightblue")  # User nodes
            node_sizes.append(300)

    # Draw the graph
    pos = nx.spring_layout(graph, k=0.8)  # Adjust spacing with `k`
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=node_sizes)

    # Draw authorship edges
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=[(u, v) for u, v, data in graph.edges(data=True) if data["edge_type"] == "authorship"],
        arrowstyle="->",
        arrowsize=20,
        edge_color="blue",
        label="Authorship",
    )

    # Draw viewership edges
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=[(u, v) for u, v, data in graph.edges(data=True) if data["edge_type"] == "viewership"],
        arrowstyle="->",
        arrowsize=10,
        edge_color="gray",
        style="dashed",
        label="Viewership",
    )

    # Add labels
    nx.draw_networkx_labels(graph, pos, font_size=10)

    # Add title and legend
    plt.title(f"Social Media Network (Importance: {criteria.capitalize()})")
    plt.legend(
        loc="upper left",
        handles=[
            plt.Line2D([0], [0], color="blue", lw=2, label="Authorship"),
            plt.Line2D([0], [0], color="gray", lw=2, linestyle="dashed", label="Viewership"),
        ],
    )
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
    add_user("taylor", {"real_name": "Taylor Jackson", "age": 23, "location": "Maui"})

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

    # Make posts
    post1 = create_post("alice", "Hello, world!")
    post2 = create_post("carol", "Excited about the new project!")
    post3 = create_post("eve", "Just moved to Oahu, loving it here!")
    post4 = create_post("bob", "Just finished a great book!")

    # People view posts
    view_post("bob", post1)
    view_post("alice", post1)
    view_post("maria", post1)
    view_post("james", post1)
    view_post("eve", post1)

    view_post("dave", post2)
    view_post("eve", post2)

    view_post("alice", post3)
    view_post("bob", post3)
    view_post("james", post3)
    view_post("carol", post3)
    view_post("dave", post3)
    view_post("eve", post3)
    view_post("maria", post3)
    view_post("taylor", post3)

    # People comment on posts
    comment_on_post("bob", post1, "Nice post!")
    comment_on_post("alice", post1, "Awesome!")
    comment_on_post("eve", post1, "Super cool.")
    comment_on_post("maria", post1, "Splendid.")
    comment_on_post("james", post1, "Cool!")

    comment_on_post("dave", post2, "Looking forward to it!")

    comment_on_post("alice", post3, "Oahu is amazing!")
    comment_on_post("carol", post3, "Love it!!")
    comment_on_post("bob", post3, "Sick!")

    # Draw the social network graph
    # Example Usage: Highlight posts based on comments / views
    draw_network(criteria="comments")

    user_posts = social_network.nodes["alice"]["posts"]
    first_post = user_posts[0]
    comments = first_post["comments"]
    for comment in comments:
      print(f"User: {comment['user']}, Comment: {comment['content']}, Time: {comment['creation_time']}")