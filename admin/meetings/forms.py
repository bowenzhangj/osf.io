from django import forms
from django.core.validators import validate_email

from modularodm import Q
from framework.auth.core import get_user
from website.models import Conference
from website.conferences.exceptions import ConferenceError


class MultiEmailField(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        return [r.strip() for r in value.split(',')]

    def validate(self, value):
        super(MultiEmailField, self).validate(value)
        for email in value:
            validate_email(email)


class MeetingForm(forms.Form):
    # Value to tell if this is being created or is an edit
    edit = forms.BooleanField(
        label='edit',
        initial=False,
        required=False,
        widget=forms.HiddenInput(),
    )
    endpoint = forms.CharField(
        label='Endpoint (Unique, short id)',
        required=True,
    )
    name = forms.CharField(
        label='Conference name',
        required=True,
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    info_url = forms.CharField(
        label='Info url',
        required=True,
        widget=forms.TextInput(attrs={'size': '60'}),
    )
    logo_url = forms.CharField(
        label='Logo url',
        required=False,
        widget=forms.TextInput(attrs={'size': '60'}),
    )
    active = forms.BooleanField(
        label='Conference is active',
        required=True,
        initial=True,
    )
    admins = MultiEmailField(
        label='Conference administrator emails (comma separated)',
        widget=forms.TextInput(attrs={'size': '50'}),
    )
    public_projects = forms.BooleanField(
        label='Projects are public',
        required=True,
        initial=True,
    )
    poster = forms.BooleanField(
        label='Posters',
        required=True,
        initial=True,
    )
    talk = forms.BooleanField(
        label='Talks',
        required=True,
        initial=True,
    )
    field_submission1 = forms.CharField(
        label='Name for Submission 1 (poster)'
    )
    field_submission2 = forms.CharField(
        label='Name for Submission 2 (talk)'
    )
    field_submission1_plural = forms.CharField(
        label='Plural for submission 1'
    )
    field_submission2_plural = forms.CharField(
        label='Plural for submission 2'
    )
    field_meeting_title_type = forms.CharField(
        label='Title for the type of meeting'
    )
    field_add_submission = forms.CharField(
        label='Add submission'
    )
    field_mail_subject = forms.CharField(
        label='Mail subject'
    )
    field_mail_message_body = forms.CharField(
        label='Message body for mail',
        widget=forms.TextInput(attrs={'size': '60'}),
    )
    field_mail_attachment = forms.CharField(
        label='Mail attachment message',
        widget=forms.TextInput(attrs={'size': '60'}),
    )

    def clean_endpoint(self):
        data = self.cleaned_data['endpoint']
        if self.data.get('edit') == 'False':
            if Conference.find(Q('endpoint', 'iexact', data)).count() > 0:
                raise forms.ValidationError(
                    'A meeting with this endpoint exists already.'
                )
        else:
            try:
                Conference.get_by_endpoint(data)
            except ConferenceError:
                raise forms.ValidationError(
                    'Meeting not found with this endpoint to update'
                )
        return data

    def clean_admins(self):
        data = self.cleaned_data['admins']
        for email in data:
            user = get_user(email=email)
            if not user or user is None:
                raise forms.ValidationError(
                    '{} does not have an OSF account'.format(email)
                )
        return data
