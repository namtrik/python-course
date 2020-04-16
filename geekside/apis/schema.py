from graphene import ObjectType, String, Schema
from .blog_schema import Query as BlogQuery, Mutation as BlogMutation
from .auth_schema import Mutation as AuthMutation

class Query(BlogQuery):
  # hello = String(name=String(default_value="stranger"))

  # def resolve_hello(root, info, name, *args, **kwargs):
  #   return 'Hello %s' % name
  pass

class Mutation(BlogMutation, AuthMutation):
  pass

ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)
