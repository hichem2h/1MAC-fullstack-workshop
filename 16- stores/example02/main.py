import models, stores

member1 = models.Member("Ahmed", 20)
member2 = models.Member("Mahmoud", 32)

members = member1, member2
member_store = stores.MemberStore()

post1 = models.Post("Post1", "Content1")
post2 = models.Post("Post2", "Content2")
post3 = models.Post("Post3", "Content3")

posts = post1, post2, post3
post_store = stores.PostStore()

for m in members:
    member_store.add(m)

print(member_store.get_all())

for p in posts:
    post_store.add(p)

print(post_store.get_all())
