#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
class project_task_model_inherit(models.Model):
    _inherit = 'project.task'
    def action_print_report_client_status(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, context=context)
        res = res and res[0] or {}
        datas.update({'form':res})
        return self.pool['report'].get_action(cr, uid, ids, 'latitude_report.client_status_report', data=datas, context=context)

    def action_print_friday_report_client_status(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        #datas = {'ids': context.get('active_ids', [])}
        datas = {'ids': uid}
        res = self.read(cr, uid, ids, context=context)
        res = res and res[0] or {}
        datas.update({'form':res})
        return self.pool['report'].get_action(cr, uid, ids, 'latitude_report.client_status_friday_report', data=datas, context=context)