import media
import fresh_tomatoes


#Instantiate Movie objects
inception = media.Movie("Inception",
                        """What happens if you die in a dream within a dream?
                        To find out, we must go deeper""",
                        "http://www.impawards.com/2010/posters/inception_ver3_xlg.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")
                        
almost_famous = media.Movie("Almost Famous",
                            """A teenage journalist on tour with an up and
                            coming band""",
                            "https://upload.wikimedia.org/wikipedia/en/d/dd/Almost_famous_poster1.jpg",
                            "https://www.youtube.com/watch?v=qk0XnyrENrE")

pans_labyrinth = media.Movie("Pan's Labyrinth",
                             "A magical faun leads a girl through a maze",
                             "http://www.impawards.com/2006/posters/pans_labyrinth_ver6.jpg",
                             "https://www.youtube.com/watch?v=EqYiSlkvRuw")

king_lines = media.Movie("King Lines",
                         "Chris Sharma searches for the world's best routes",
                         "http://www.bigupproductions.com/wp-content/files_mf/1334939547KingLines_Cover_fullres.jpg",
                         "https://www.youtube.com/watch?v=3vEJS2AwGA8")

forgetting_sarah_marshall = media.Movie("Forgetting Sarah Marshall",
                                        """A man goes on vacation to deal with
                                        a breakup and runs into his ex.
                                        Hilarity ensues.""",
                                        "http://www.impawards.com/2008/posters/forgetting_sarah_marshall_ver3_xlg.jpg",
                                        "https://www.youtube.com/watch?v=PyVEHIO6jZ0")

ten_things_i_hate_about_you = media.Movie("10 Things I Hate About You",
                                          "A modern retelling of Shakepeare's"
                                          " \"Taming of the Shrew\"",
                                          "https://upload.wikimedia.org/wikipedia/en/9/95/10_Things_I_Hate_About_You_film.jpg",
                                          "https://www.youtube.com/watch?v=AWmjzCZr0Jw")

#Put above movies into a list
movies = [inception, almost_famous, pans_labyrinth, king_lines,
          forgetting_sarah_marshall, ten_things_i_hate_about_you]

#Generate website
fresh_tomatoes.open_movies_page(movies)
