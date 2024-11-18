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

    # Additional posts
    post4 = create_post("bob", "Just finished a great book!")
    post5 = create_post("taylor", "Had an amazing dinner last night.")
    post6 = create_post("james", "Started a new job today!")
    post7 = create_post("maria", "Enjoying a sunny day at the beach.")
    post8 = create_post("carol", "Learning to cook new recipes.")
    post9 = create_post("dave", "Just ran a marathon!")
    post10 = create_post("eve", "Exploring the city.")
    post11 = create_post("alice", "Reading a fascinating article.")
    post12 = create_post("bob", "Watching a new movie.")
    post13 = create_post("taylor", "Attending a concert tonight.")
    post14 = create_post("james", "Working on a new project.")
    post15 = create_post("maria", "Visiting family this weekend.")
    post16 = create_post("carol", "Trying out a new hobby.")
    post17 = create_post("dave", "Just adopted a puppy!")
    post18 = create_post("eve", "Planning a trip to Europe.")
    post19 = create_post("alice", "Enjoying a quiet evening at home.")
    post20 = create_post("bob", "Just finished a workout.")
    post21 = create_post("taylor", "Had a terrible day at work.")
    post22 = create_post("james", "Feeling frustrated with everything.")
    post23 = create_post("maria", "Excited for the weekend!")
    post24 = create_post("carol", "Just bought a new car.")
    post25 = create_post("dave", "Celebrating a friend's birthday.")

    # Posts with profanity
    post26 = create_post("eve", "This is a damn good coffee!")
    post27 = create_post("alice", "What the hell is going on?")

    comment_on_post("bob", post4, "Sounds interesting!")
    comment_on_post("taylor", post5, "Yum!")
    comment_on_post("james", post6, "Congrats!")
    comment_on_post("maria", post7, "Enjoy!")
    comment_on_post("dave", post8, "Nice!")
    comment_on_post("carol", post9, "Great job!")
    comment_on_post("eve", post10, "Have fun!")
    comment_on_post("alice", post11, "Interesting read.")
    comment_on_post("bob", post12, "How was it?")
    comment_on_post("taylor", post13, "Have a great time!")
    comment_on_post("james", post14, "Good luck!")
    comment_on_post("maria", post15, "Safe travels!")
    comment_on_post("dave", post16, "Enjoy your new hobby!")
    comment_on_post("carol", post17, "Congrats on the new puppy!")
    comment_on_post("eve", post18, "Have a great trip!")
    comment_on_post("alice", post19, "Sounds relaxing.")
    comment_on_post("bob", post20, "Great job!")
    comment_on_post("taylor", post21, "Sorry to hear that.")
    comment_on_post("james", post22, "Hang in there.")
    comment_on_post("maria", post23, "Me too!")
    comment_on_post("dave", post24, "Congrats on the new car!")
    comment_on_post("carol", post25, "Happy birthday to your friend!")
    comment_on_post("eve", post26, "Glad you like it!")
    comment_on_post("alice", post27, "I know, right?")

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