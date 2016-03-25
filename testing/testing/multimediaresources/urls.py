# Copyright (c) 2010-2013 by Yaco Sistemas <goinnn@gmail.com> or <pmartin@yaco.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.

try:
    from django.conf.urls import include, url
except ImportError:  # Django < 1.4
    from django.conf.urls.defaults import include, url

from testing.multimediaresources import views

urlpatterns = [
    url(r'^$', views.multimediaresources_index, name='multimediaresources_index'),
    url(r'^(?P<resource_id>\w+)/$', views.multimediaresources_edit, name="multimediaresources_edit"),
]
