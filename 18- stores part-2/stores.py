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
