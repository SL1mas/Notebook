from app import db
from models import *

db.create_all()


note1 = Note("Title", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note2 = Note("Even lnger then medium size title",
             "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note3 = Note("This one is unusally long author probably wanted to show something",
             "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note4 = Note("Medium size title", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note5 = Note("Title", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note6 = Note("Medium size title", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note7 = Note("Even lnger then medium size title",
             "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note8 = Note("Title", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note9 = Note("This one is unusally long author probably wanted to show something",
             "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note10 = Note("Medium size title", "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note11 = Note("This one is unusally long author probably wanted to show something",
              "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)
note12 = Note("Even lnger then medium size title",
              "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate, in quibusdam vero maxime voluptas minus ea ab placeat odio nam eos libero tenetur eius. Nulla excepturi esse adipisci quo tenetur.", 1)

db.session.add_all([note1, note2, note3, note4, note5, note6,
                   note7, note8, note9, note10, note11, note12])


category1 = Category("Transport")
category2 = Category("Hobbies")
category3 = Category("Sports")
category4 = Category("Music")
category5 = Category("Traveling")

db.session.add_all([category1, category2, category3, category4, category5])

user1 = User("Simas", "test@test.lt",
             "$2b$12$iMwKbXrQCW3LTWxTZ7jZjuN4sSLdOYt28dss1K/u2FvZvV4AaMBOW")
user2 = User("Petras", "test2@test.lt",
             "$2b$12$QjDQANxR.05rXWIQlkZgGO47ZluYnXucCGsw2K45PCU5UXDsK6/7a")
db.session.add_all([user1, user2])

db.session.commit()
