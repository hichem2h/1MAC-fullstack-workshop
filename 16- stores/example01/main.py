from models import Member, Post
from stores import MemberStore, PostStore

member1 = Member("Ahmed", 20)
member2 = Member("Mahmoud", 32)

post1 = Post("Post1", "Content1")
post2 = Post("Post2", "Content2")
post3 = Post("Post3", "Content3")

# Member Store
member_store = MemberStore()

member_store.add(member1)
member_store.add(member2)

print(member_store.get_all())

# Post Store
post_store = PostStore()

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print(post_store.get_all())
