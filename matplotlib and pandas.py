import pandas as pd
import matplotlib.pyplot as plt


def main(file_name):
    games = pd.read_csv(file_name)     #read from CSV file to get my information
    games = games.dropna()             # getting rid of the games that do not have publishers, because they are not needed for my graphs

#----------------------------------------

    #This bar graph shows which producers made the most games during the years of 2004 till 2008. Now just because EA made a ton of games
    # that does not mean they are all great games. Big companies like EA are always making tons of games
    # Some of the smaller publishers actually have some connection to EA if you look closely. Kind of like how Dice and EA both make the Battlefield series of games


    plt.subplot(121)
    plt.title("test")
    sums = games.groupby(games["Metadata.Publishers"])["Metadata.Publishers"].count()   # adding up each time a company made a game
    plot_x = plt.ylabel("Amount of Games Made")
    plot_y = plt.xlabel("Publisher")
    sums.plot(x=plot_x, y=plot_y, kind="bar", title="Amount of Games Each Publisher Makes", color=tuple(["blue", "orange"]))   #plotting the number of games each company made

#----------------------------------------

    # This line graph shows the overall trend of video game creation rising. Probably due to the fact that more and more people started to like video games
    # This was also the time when the PS3 and Xbox 360 were either being developed or being released, so there was a lot of competition to produce lots of games between the two.
    # I would suspect this line would still be rising today because lots of people play video games.

    plt.subplot(122)
    year = games["Release.Year"]        # creating a list of all the games made per year
    plot_second_y = plt.ylabel("Year")
    plot_second_x = plt.xlabel("Amount of Games")
    year.plot(x=plot_second_x, y=plot_second_y, kind="line", title="Amount of Games Made per Year", color="blue", yticks=[2004, 2005, 2006, 2007, 2008]) #plotting a line of all the games made per year


    plt.show()


main("video_games.csv")

