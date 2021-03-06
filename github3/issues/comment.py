# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .. import users
from ..utils import timestamp_parameter
from ..models import BaseComment


class IssueComment(BaseComment):
    """The :class:`IssueComment <IssueComment>` object. This structures and
    handles the comments on issues specifically.

    Two comment instances can be checked like so::

        c1 == c2
        c1 != c2

    And is equivalent to::

        c1.id == c2.id
        c1.id != c2.id

    See also: http://developer.github.com/v3/issues/comments/
    """
    def _update_attributes(self, comment):
        super(IssueComment, self)._update_attributes(comment)

        #: :class:`User <github3.users.User>` who made the comment
        self.user = self._class_attribute(
            comment, 'user', users.ShortUser, self,
        )

        #: Issue url (not a template)
        self.issue_url = self._get_attribute(comment, 'issue_url')

        #: Html url (not a template)
        self.html_url = self._get_attribute(comment, 'html_url')

    def _repr(self):
        return '<Issue Comment [{0}]>'.format(self.user.login)


def issue_comment_params(sort, direction, since):
    params = {}

    if sort in ('created', 'updated'):
        params['sort'] = sort

    if direction in ('asc', 'desc'):
        params['direction'] = direction

    since = timestamp_parameter(since)
    if since:
        params['since'] = since

    return params
