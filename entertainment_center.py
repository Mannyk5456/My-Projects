import media
import webbrowser
import fresh_tomatoes

dark_knight = media.Movie("Dark Knight",
                          "With the help of allies Lt. Jim Gordon and DA Harvey Dent, Batman has been able to keep a tight lid on crime in Gotham City. But when a vile young criminal calling himself the Joker (Heath Ledger) suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://youtu.be/kmJLuwP3MbY")
#dark_knight.show_trailer()

spider_man = media.Movie("Spider Man",
                        "With great Power comes great Responsibility",
                        "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
                        "https://www.youtube.com/watch?v=O7zvehDxttM")

harry_potter = media.Movie("Harry Potter",
                        "The Story of a boy who is the orphaned son of two powerful wizards and possesses unique magical powers of his own.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
                        "https://youtu.be/PbdM1db3JbY")

Matrix = media.Movie("Matrix",
                        "Neo believes that Morpheus, an elusive figure considered to be the most dangerous man alive, can answer his question -- What is the Matrix?",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://youtu.be/vKQi3bBA1y8")

few_good_men = media.Movie("A Few Good Men",
                        "Lt. Daniel Kaffee is a military lawyer defending two U.S. Marines charged with killing a fellow Marine at the Guantanamo Bay Naval Base in Cuba.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSYAB38F7l03EtFMcKKFH4_TQcyBbbETDdreBvbVX30UQ0bsg8L",
                        "https://youtu.be/sCrR9uQrPKA")

star_wars = media.Movie("Star Wars Episode V: The Empire Strikes Back",
                     "The adventure continues in this 'Star Wars' sequel. Luke Skywalker, Han Solo, Princess Leia and Chewbacca face attack by the Imperial forces and its AT-AT walkers on the ice planet Hoth",
                     "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                     "https://youtu.be/JNwNXF9Y6kY")


movies = [dark_knight, spider_man, harry_potter, Matrix, few_good_men,star_wars]
fresh_tomatoes.open_movies_page(movies)
