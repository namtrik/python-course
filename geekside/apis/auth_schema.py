from graphene import ObjectType
import graphql_jwt
from django import forms
from django.core.mail import EmailMultiAlternatives

class EmailForm(forms.Form):
  subject = forms.CharField(min_length=5, max_length=64)
  message = forms.CharField(min_length=20)

  def save(self, *args, **kwargs):
    subject = self.cleaned_data['subject']
    message = self.cleaned_data.get('message')
    body_text = "Hola \n%s" % message
    sender = 'djangoemailtestdemo@gmail.com'
    to = ['rijic15494@emailhost99.com']
    body_html = """
    <div style="background: black; color: white; height: 100px;">
    %s
    </div>
    """ % message

    email_message = EmailMultiAlternatives(subject=subject,
      body=body_text, from_email=sender, to=to)
    email_message.attach_alternative(body_html, 'text/html')
    # email_message.attach()
    email_message.send()

from graphene_django.forms.mutation import DjangoFormMutation
class EmailMutation(DjangoFormMutation):
  class Meta:
    form_class = EmailForm

class Mutation(ObjectType):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()
  send_mail = EmailMutation.Field()
