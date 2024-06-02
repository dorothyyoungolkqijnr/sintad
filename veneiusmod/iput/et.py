for user in users:
    # print the user's name
    print(user.name)
    # update the user's profile with a new score
    user.score += 10
    # save the user's profile to a file
    user.save()
