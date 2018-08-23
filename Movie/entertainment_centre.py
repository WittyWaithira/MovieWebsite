import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
avatar = media.Movie("Avatar","A marine on an alien planet","https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

#avatar.show_trailer()
hunger_games = media.Movie("Hunger Games","A reality show",
                           "https://www.google.com/search?q=hunger+games+images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjk5K7rgIHdAhWENOwKHaWkDXAQ_AUICigB&biw=1517&bih=735#imgrc=NdAylPnjADX_kM:","https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story,avatar,hunger_games]

fresh_tomatoes.open_movies_page(movies)

