#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2007  Donald N. Allingham
# Copyright (C) 2007-2008  Brian G. Matherly
# Copyright (C) 2008  Jerome Rapinat
# Copyright (C) 2008  Benny Malengier
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# gen.filters.rules/_HasNoteBase.py
# $Id$
#

#-------------------------------------------------------------------------
#
# Standard Python modules
#
#-------------------------------------------------------------------------
from ...ggettext import gettext as _

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from . import Rule

#-------------------------------------------------------------------------
# "Objects having notes"
#-------------------------------------------------------------------------
class HasNoteBase(Rule):
    """Objects having notes"""

    labels      = [  _('Number of instances:'), _('Number must be:')]
    name        = 'Object with notes'
    description = "Matches objects that have a certain number of notes"
    category    = _('General filters')

    def __init__(self, arg):
        # Upgrade from pre 3.1 HasNote filter, use defaults that correspond
        # Previous filter had 0 arguments
        if len(arg) == 0:
            Rule.__init__(self, ["0", 'greater than'])
        else:
            Rule.__init__(self, arg)

    def prepare(self, db):
        # things we want to do just once, not for every handle
        if  self.list[1] == 'lesser than':
            self.count_type = 0
        elif self.list[1] == 'greater than':
            self.count_type = 2
        else:
            self.count_type = 1 # "equal to"

        self.userSelectedCount = int(self.list[0])


    def apply(self, db, obj):
        count = len( obj.get_note_list())
        if self.count_type == 0:     # "lesser than"
            return count < self.userSelectedCount
        elif self.count_type == 2:   # "greater than"
            return count > self.userSelectedCount
        # "equal to"
        return count == self.userSelectedCount
