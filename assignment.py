import networkx as nx
from datetime import datetime, timedelta
import random

# Initialize the social network graph
social_network = nx.DiGraph()

# Add a user to the social network
def add_user(user_name, attributes=None):
    if attributes is None:
        attributes = {}
    social_network.add_node(user_name, attributes=attributes, posts=[], seen_posts=[], comments=[])

# Create a post for a user
def create_post(user_name, content):
    post = {
        "content": content,
        "creation_time": datetime.now(),
        "comments": [],
        "views": []
    }
    social_network.nodes[user_name]["posts"].append(post)
    return post

# Record a user viewing a post
def view_post(user_name, post):
    if post not in social_network.nodes[user_name]["seen_posts"]:
        social_network.nodes[user_name]["seen_posts"].append(post)
    post["views"].append({"user": user_name, "view_time": datetime.now()})

# Identify trending posts with filters
def trending_posts(
    time_window_hours=24, 
    include_keywords=None, 
    exclude_keywords=None, 
    user_attribute_filters=None
):
    current_time = datetime.now()
    trending = []

    for node, data in social_network.nodes(data=True):
        # Apply user attribute filters
        if user_attribute_filters:
            if not all(data["attributes"].get(attr) == value for attr, value in user_attribute_filters.items()):
                continue

        for post in data["posts"]:
            # Apply keyword filters
            if include_keywords and not any(keyword in post["content"] for keyword in include_keywords):
                continue
            if exclude_keywords and any(keyword in post["content"] for keyword in exclude_keywords):
                continue

            # Count recent views
            recent_views = [
                view for view in post["views"]
                if current_time - view["view_time"] <= timedelta(hours=time_window_hours)
            ]
            trending.append({
                "post": post,
                "author": node,
                "view_count": len(recent_views)
            })

    # Sort posts by view count in descending order
    trending.sort(key=lambda x: x["view_count"], reverse=True)
    return trending

# Test the implementation with uneven view distribution
if __name__ == "__main__":
    # Add users
    add_user("alice", {"real_name": "Alice Smith", "age": 30, "location": "Oahu", "gender": "Female"})
    add_user("bob", {"real_name": "Bob Jones", "age": 25, "location": "Oahu", "gender": "Male"})
    add_user("carol", {"real_name": "Carol White", "age": 35, "location": "Oahu", "gender": "Female"})
    add_user("dave", {"real_name": "Dave Brown", "age": 28, "location": "Maui", "gender": "Male"})
    add_user("eve", {"real_name": "Eve Davis", "age": 22, "location": "Oahu", "gender": "Female"})
    add_user("james", {"real_name": "James Smith", "age": 19, "location": "Kauai", "gender": "Male"})
    add_user("maria", {"real_name": "Maria Garcia", "age": 23, "location": "Oahu", "gender": "Female"})
    add_user("william", {"real_name": "William Johnson", "age": 20, "location": "Maui", "gender": "Male"})
    add_user("taylor", {"real_name": "Taylor Jackson", "age": 22, "location": "Maui", "gender": "Female"})


    # Create posts
    posts = []
    posts.append(create_post("alice", "Exploring beautiful Oahu!"))
    posts.append(create_post("bob", "What a damn good day!"))
    posts.append(create_post("carol", "Learning Python is fucking fun!"))
    posts.append(create_post("dave", "Just finished hiking a volcano."))
    posts.append(create_post("eve", "Loving life on the islands!"))
    posts.append(create_post("eve", "This island is amazing, hell yeah!"))
    posts.append(create_post("james", "Learning photography to capture island beauty."))
    posts.append(create_post("james", "Reading about Hawaiian history."))
    posts.append(create_post("maria", "Excited to start a new adventure!"))
    posts.append(create_post("maria", "Learning how to bake this weekend."))
    posts.append(create_post("william", "Attending a cultural event in Maui."))
    posts.append(create_post("william", "Learning to cook traditional Hawaiian dishes."))
    posts.append(create_post("taylor", "Scuba diving in Maui is so much fun!"))
    posts.append(create_post("taylor", "Enjoying a calm evening on the beach."))

    # Simulate uneven views
    viewers = ["alice", "bob", "carol", "dave", "eve", "james", "maria", "william", "taylor"]
    for post in posts:
        # Randomize number of views (1 to 200 per post)(Adjustable)
        # For testing purposes only, simulating a real-world scenario(Too much work to input each user's view manually)
        for _ in range(random.randint(1, 200)):
            viewer = random.choice(viewers)
            view_post(viewer, post)

    # Trending posts report
    # Test 1: Trending Posts (Location: Oahu, Without Profanity)
    print("\nTop 3 Trending Posts (Location: Oahu, Without Profanity):")
    trending_oahu_no_profanity = trending_posts(
        time_window_hours=24,
        exclude_keywords=["damn", "hell", "fucking"],
        user_attribute_filters={"location": "Oahu"}
    )
    for trend in trending_oahu_no_profanity[:3]:  # Display only the top 3 posts(Changable to any number of posts you want to display)
        print(f"Author: {trend['author']}, Content: {trend['post']['content']}, Views: {trend['view_count']}")
    
    # Test 2: Trending Posts Including the Word 'Island'
    print("\nTop 3 Trending Posts Including the Word 'Island':")
    trending_island = trending_posts(
        time_window_hours=24,
        include_keywords=["island"]
    )
    for trend in trending_island[:3]:  # Display only the top 3 posts(Changable to any number of posts you want to display)
        print(f"Author: {trend['author']}, Content: {trend['post']['content']}, Views: {trend['view_count']}")

    # Test 3: Trending Posts for Users Based on Age and Gender
    print("\nTop 3 Trending Posts (Female Users Aged 22):")
    trending_females_age_22 = trending_posts(
        time_window_hours=24,
        user_attribute_filters={"gender": "Female", "age": 22}  
    )
    for trend in trending_females_age_22[:3]:  # Display only the top 3 posts(Changable to any number of posts you want to display)
        print(f"Author: {trend['author']}, Content: {trend['post']['content']}, Views: {trend['view_count']}")
