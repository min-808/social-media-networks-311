import re
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from wordcloud import WordCloud
from collections import Counter
from better_profanity import profanity

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
    add_user("william", {"real_name": "William Johnson", "age": 20, "location": "Maui"})
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
    post26 = create_post("eve", "This is a damn good coffee!")
    post27 = create_post("alice", "What the hell is going on?")
    post28 = create_post("taylor", "Reflecting on the past year, I've realized how much I've grown and learned. Grateful for all the experiences, both good and bad.")
    post29 = create_post("james", "Just finished reading an incredible book on personal development. Highly recommend it to anyone looking to improve themselves.")
    post30 = create_post("maria", "Spent the entire day hiking through the mountains. The views were absolutely breathtaking and the fresh air was invigorating.")
    post31 = create_post("carol", "Experimenting with new recipes has been so much fun! Today I made a delicious homemade pizza from scratch.")
    post32 = create_post("dave", "Participated in a charity run this morning. It was a great way to stay active and support a good cause.")
    post33 = create_post("eve", "Exploring the hidden gems of the city has been an adventure. Found a quaint little coffee shop that serves the best lattes.")
    post34 = create_post("alice", "Diving into a new hobby: painting. It's been a relaxing and creative outlet for me.")
    post35 = create_post("bob", "Just watched an inspiring documentary about the power of community and collaboration.")
    post36 = create_post("taylor", "Attended a virtual conference on technology and innovation. Learned so much about the future of AI and its potential impact.")
    post37 = create_post("james", "Feeling overwhelmed with work, but taking it one step at a time. Remembering to breathe and stay positive.")
    post38 = create_post("maria", "Spent the weekend with family, sharing stories and laughter. It's moments like these that I cherish the most.")
    post39 = create_post("carol", "Tried my hand at gardening today. Planted some flowers and herbs, and can't wait to see them grow.")
    post40 = create_post("dave", "Just adopted a rescue dog. He's a bundle of energy and has already brought so much joy into my life.")
    post41 = create_post("eve", "Planning a trip to Europe next summer. Excited to explore new cultures and cuisines.")
    post42 = create_post("alice", "Enjoying a quiet evening at home with a good book and a cup of tea.")
    post43 = create_post("bob", "Just finished a challenging workout. Feeling accomplished and ready to tackle the day.")
    post44 = create_post("taylor", "Had a tough day at work, but grateful for the support of my friends and family.")
    post45 = create_post("james", "Feeling frustrated with the current situation, but trying to stay hopeful and look for solutions.")
    post46 = create_post("maria", "Excited for the weekend! Planning to catch up on some much-needed rest and relaxation.")
    post47 = create_post("carol", "Just bought a new car. Cannot wait to take it for a spin and explore new places.")
    post48 = create_post("dave", "Celebrating a friend's birthday tonight. Looking forward to good food, good company, and lots of laughter.")
    post49 = create_post("eve", "This is a damn good coffee! Found a new favorite spot to get my caffeine fix.")
    post50 = create_post("alice", "What the hell is going on? Feeling confused and trying to make sense of everything.")
    post51 = create_post("carol", "Exploring the latest advancements in technology. It is amazing how fast things are evolving.")
    post52 = create_post("dave", "Just attended a tech meetup. Learned a lot about blockchain and its potential applications.")
    post53 = create_post("eve", "Reading about the impact of technology on education. It is fascinating to see how it is transforming learning.")
    post54 = create_post("alice", "Excited about the new tech gadgets coming out this year. Cannot wait to try them out.")
    post55 = create_post("taylor", "Discussing the ethical implications of AI technology. It is a complex and important topic.")
    post56 = create_post("james", "Working on a project that uses cutting-edge technology. It is challenging but rewarding.")
    post57 = create_post("maria", "Attended a webinar on the future of technology in healthcare. The possibilities are endless.")
    post58 = create_post("carol", "Exploring the role of technology in environmental conservation. It is a powerful tool for change.")
    post59 = create_post("dave", "Learning about the history of technology and its impact on society. It is a fascinating journey.")
    post60 = create_post("eve", "Discussing the future of technology with friends. It is exciting to think about what is next.")


    # Draw the social network graph
    # draw_social_network()

    # Example operations on the graph:

    # Get all user's posts
    # print(f"alice's posts: {social_network.nodes['alice']['posts']}")
    
    # Get all comments under a post
    # user_posts = social_network.nodes["alice"]["posts"]
    # first_post = user_posts[0]
    # comments = first_post["comments"]
    # for comment in comments:
    #   print(f"User: {comment['user']}, Comment: {comment['content']}, Time: {comment['creation_time']}")

    # # Get all views of a post
    # print(f"User: post1 has {len(post1['views'])} views")

    # # Get the follower count of a user
    # user_followers = social_network.in_degree("bob")
    # print(f"User: bob has {user_followers} followers")
    
# Ensure profanity library is initialized
profanity.load_censor_words()
def generateWordCloud(
  social_network, 
  includeKeywords=None, 
  excludeKeywords=None, 
  userAttributes=None, 
  censorProfanity=True
  minWordLength=3,
):
  filteredContentArr = []

  for user in social_network.nodes:
    # Check if user attributes match
    if userAttributes:
      match = all(userAttributes.get(attr) == social_network.nodes[user].get(attr) for attr in userAttributes)
      if not match:
        continue

    for post in social_network.nodes[user]['posts']:
      content = post['content']
      
      # Filter posts based on include and exclude keywords
      if includeKeywords and not any(keyword in content for keyword in includeKeywords):
        continue
      if excludeKeywords and any(keyword in content for keyword in excludeKeywords):
        continue
      # Filter out profanity
      if censorProfanity:
        content = profanity.censor(content)
        
      filteredContentArr.append(content)

  # Debug: Print the filtered content
  # print("Filtered Content Array:", filteredContentArr)
  
  filteredContentStr = ' '.join(filteredContentArr)
  
  # Remove all symbols and apostrophes
  filteredContentStr = re.sub(r"[^\w\s]", "", filteredContentStr).replace("'", "")
  allWords = filteredContentStr.split()
  
  allWords = [word for word in allWords if len(word) > minWordLength]
    
  allWordsSpaced = ' '.join(allWords)
  
  print("All Words:", allWordsSpaced)

  # Count the occurrences of each word
  wordCounters = Counter(re.findall(r'\w+', allWordsSpaced))

  # print("Word Counters:", wordCounters)

  # Get the top 25 words
  top25 = [word for word, count in wordCounters.most_common(25)]

  print("Top 25 Words:", top25)

  # Filter allContentStr to only include the top 25 words
  wordCloudString = ' '.join([word for word in re.findall(r'\w+', allWordsSpaced) if word in top25])

  # Debug: Print the word cloud string
  print("Word Cloud String:", wordCloudString)

  # Generate a word cloud image
  wordCloud = WordCloud(max_font_size=40).generate(wordCloudString)

  # Display the generated image
  plt.imshow(wordCloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()

generateWordCloud(social_network)
