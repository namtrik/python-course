from graphene_django import DjangoObjectType
from blog.models import Category as CategoryModel, Post as PostModel
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField

class Category(DjangoObjectType):
  """Nodo del grago"""
  class Meta:
    model = CategoryModel
    # filter_fields = ['name', 'is_active']
    filter_fields = {
      'name': ['exact', 'icontains', 'istartswith'],
      'is_active': ['exact']
    }
    # exclude = ['post_set']
    interfaces = (relay.Node, )

class Post(DjangoObjectType):
  class Meta:
    model = PostModel
    filter_fields = {
      'title': ['exact', 'icontains', 'istartswith'],
      'text': ['icontains'],
      'excerpt': ['icontains'],
      'is_active': ['exact'],
      'category__name': ['exact', 'icontains'],
      'created_at': ['gt', 'gte', 'lt', 'lte']
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  """consultas de la app blog"""
  categories = DjangoFilterConnectionField(Category)
  category = relay.Node.Field(Category)

  posts = DjangoFilterConnectionField(Post)
  post = relay.Node.Field(Post)

  from graphql_jwt.decorators import login_required
  @login_required
  def resolve_categories(self, info, *args, **kwargs):
    return CategoryModel.objects.filter(**kwargs)

from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from blog.forms import CategoryModelForm, PostModelForm
class CategoryMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CategoryModelForm

class Mutation(ObjectType):
  category = CategoryMutation.Field()
