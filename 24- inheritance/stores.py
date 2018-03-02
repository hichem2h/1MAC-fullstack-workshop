import itertools

class BaseStore():

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, member):
        member.id = self._last_id
        self._data_provider.append(member)
        self._last_id += 1

    def get_by_id(self, id):
        result = None
        all_model_instances = self.get_all()
        for e in all_model_instances:
            if e.id == id :
                result = e
                break
        return result

    def entity_exists(self, model_instance):
        result = False
        if self.get_by_id(model_instance.id) is not None:
            result = True
        return result

    def delete(self, id):
        model_instance = self.get_by_id(id)
        all_model_instances = self.get_all()
        all_model_instances.remove(model_instance)

    def update(self, model_instance):
        all_model_instances = self.get_all()
        for i, p in enumerate(all_model_instances):
            if model_instance.id == p.id:
                all_model_instances[i] = model_instance
                break


class MemberStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)

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


class PostStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostStore.posts, PostStore.last_id)

    def get_posts_by_date(self):
        all_posts = self.get_all() [:]
        all_posts.sort(key=lambda x: x.date, reverse=True)
        for post in all_posts:
            yield post
