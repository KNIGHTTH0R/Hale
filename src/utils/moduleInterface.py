################################################################################
#   (c) 2010, The Honeynet Project
#   Author: Patrik Lantz  patrik@pjlantz.com
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
################################################################################

import abc

class Module(object):
    """
    Defines what methods must be implemented
    for the different modules
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getConfig(self):
        """
        Return configuration used by this module
        """
        
        return

    @abc.abstractmethod
    def stop(self):
        """
        To be implemented in the various modules. Used since threadManager
        calls this method when stopping a module. Should basically close
        down the connection for the module.
        """
       
        return
    
    @abc.abstractmethod  
    def run(self):
        """
        Method called when threadManager starts a module
        """
        
        return
        