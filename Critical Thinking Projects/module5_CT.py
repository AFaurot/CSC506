# This class handles functions to add recommendations for users, and also update watch history.
class RecommendVideoContent:

    # Initialize two dictionaries.
    # One for user preferences and one for watch history
    def __init__(self):
        # Dictionary to store user preferences
        self.user_preferences = {}
        # Dictionary to store watch history
        self.watch_history = {}


    # Function to add video recommendations to the list
    def add_recommendation(self, user_id, video):

        # If user has no recommendations in preference dictionary
        # Initialize an empty list associated with their user
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = []
        self.user_preferences[user_id].append(video)

    # Function to update watch history
    def update_history(self, user_id, video):

        # If user exists already append video to history
        if user_id in self.watch_history:
            self.watch_history[user_id].append(video)
        # Else create the list with first entry
        else:
            self.watch_history[user_id] = [video]

    def get_recommendations(self, user_id):

        # Retrieve content
        return self.user_preferences.get(user_id, [])

    def get_history(self, user_id):

        # Retrieve history
        return self.watch_history.get(user_id, [])


def main():

    # User_id
    user_id = "aaronF"
    # Call class
    recommender = RecommendVideoContent()
    # Add recommendations
    recommender.add_recommendation(user_id, "Fishing Videos")
    recommender.add_recommendation(user_id, "Python Tutorials")

    # update watch history
    recommender.update_history(user_id, "Video XYZ")

    # print recommendations
    print(f"{user_id} recommended content: {recommender.get_recommendations(user_id)}")

    # print history
    print(f"{user_id} watch history: {recommender.get_history(user_id)}")


if __name__ == '__main__':
    main()

