import itertools

class MemberStore:
    members = []
    last_id = 1

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        result = None
        all_members = self.get_all()
        for e in all_members:
            if e.id == id :
                result = e
        return result

    def entity_exists(self, member):
        result = False
        if self.get_by_id(member.id):
            result = True
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def update(self, member):
        all_members = self.get_all()
        for i, m in enumerate(all_members):
            if member.id == m.id:
                all_members[i] = member
                break

    def get_by_name(self, name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = self.get_all() [:]

        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)
        for member in all_members:
            yield member

    def get_top_two(self, post_store):
          all_members = self.get_members_with_posts(post_store)
          all_members = sorted(all_members, key=lambda x: len(x.posts), reverse=True)
          return all_members[:2]

class PostStore:
    posts = []
    last_id = 1

    def add(self, post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_all(self):
        return PostStore.posts

    def get_by_id(self, id):
        result = None
        all_posts = self.get_all()
        for e in all_posts:
            if e.id == id :
                result = e
        return result

    def entity_exists(self, post):
        result = False
        if self.get_by_id(post.id):
            result = True
        return result

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def update(self, post):
        all_posts = self.get_all()
        for i, p in enumerate(all_posts):
            if post.id == p.id:
                all_posts[i] = post
                break
