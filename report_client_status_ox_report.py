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

import time
import datetime
from datetime import date, datetime, timedelta
from openerp.report import report_sxw
from openerp.osv import osv

class client_status_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(client_status_report, self).__init__(cr, uid, name, context)

        self.localcontext.update({
            'time': time,
            'get_data': self.get_data,
            'get_projects': self.get_projects,
            'get_date': self.get_date,
        })

        self.context = context

    def get_date(self):
        today = datetime.today()
        edate = today.strftime('%d, %b %Y')
        return edate     

    def get_projects(self):
        recsss = self.pool.get('project.project').search(self.cr,self.uid, [], context=self.context)
        resss = self.pool.get('project.project').browse(self.cr, self.uid, recsss)
        return resss    

    def get_data(self,project_id):
        recs = self.pool.get('project.task').search(self.cr,self.uid, [('project_id','=',project_id.id)], context=self.context)
        res = self.pool.get('project.task').browse(self.cr, self.uid, recs)
        info = []
        for re in res:
            if re.stage_id.name == 'Done':
                today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                dtx_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                dtx_e_obj = datetime.strptime(re.date_last_stage_update,"%Y-%m-%d %H:%M:%S")
                timedelta = dtx_s_obj - dtx_e_obj
                if timedelta.days < 8:
                    last_desc = ''
                    current_desc = ''
                    for a in re.work_ids:
                        today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                        dt_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                        dt_e_obj = datetime.strptime(a.date,"%Y-%m-%d %H:%M:%S")
                        timedelta = dt_s_obj - dt_e_obj
                        if timedelta.days > 8:
                            if len(last_desc) > 0:
                                last_desc = last_desc+' | '+a.name
                            else:
                                last_desc = a.name   
                        else:
                            if len(current_desc) > 0:
                                current_desc = current_desc+' | '+a.name
                            else:
                                current_desc = a.name    
                    data = {
                    #'project_name' : re.project_id.name,
                    'task_name' :re.name,
                    'current_desc' : current_desc,
                    'last_desc' : last_desc,
                    'description' :re.description,
                    'status' :re.stage_id.name
                    }
                    info.append(data)
            elif re.stage_id.name == 'Cancelled':
                today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                dtx_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                dtx_e_obj = datetime.strptime(re.date_last_stage_update,"%Y-%m-%d %H:%M:%S")
                timedelta = dtx_s_obj - dtx_e_obj
                if timedelta.days < 8:
                    last_desc = ''
                    current_desc = ''
                    for a in re.work_ids:
                        today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                        dt_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                        dt_e_obj = datetime.strptime(a.date,"%Y-%m-%d %H:%M:%S")
                        timedelta = dt_s_obj - dt_e_obj
                        if timedelta.days > 8:
                            if len(last_desc) > 0:
                                last_desc = last_desc+' | '+a.name
                            else:
                                last_desc = a.name   
                        else:
                            if len(current_desc) > 0:
                                current_desc = current_desc+' | '+a.name
                            else:
                                current_desc = a.name    
                    data = {
                    #'project_name' : re.project_id.name,
                    'task_name' :re.name,
                    'current_desc' : current_desc,
                    'last_desc' : last_desc,
                    'description' :re.description,
                    'status' :re.stage_id.name
                    }
                    info.append(data)        
            else:
                last_desc = ''
                current_desc = ''
                for a in re.work_ids:
                    today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                    dt_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                    dt_e_obj = datetime.strptime(a.date,"%Y-%m-%d %H:%M:%S")
                    timedelta = dt_s_obj - dt_e_obj
                    if timedelta.days > 8:
                        if len(last_desc) > 0:
                            last_desc = last_desc+' | '+a.name
                        else:
                            last_desc = a.name   
                    else:
                        if len(current_desc) > 0:
                            current_desc = current_desc+' | '+a.name
                        else:
                            current_desc = a.name    
                data = {
                #'project_name' : re.project_id.name,
                'task_name' :re.name,
                'current_desc' : current_desc,
                'last_desc' : last_desc,
                'description' :re.description,
                'status' :re.stage_id.name
                }
                info.append(data)        
        return info

           

class wrapped_report_revenewrepoert(osv.AbstractModel):
    _name = 'report.latitude_report.client_status_report'
    _inherit = 'report.abstract_report'
    _template = 'latitude_report.client_status_report'
    _wrapped_report_class = client_status_report



class client_status_friday_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(client_status_friday_report, self).__init__(cr, uid, name, context)

        self.localcontext.update({
            'time': time,
            'get_data': self.get_data,
            'get_projects': self.get_projects,
            'get_date': self.get_date,
            'get_name': self.get_name,
        })

        self.context = context

    def get_date(self):
        today = datetime.today()
        edate = today.strftime('%d, %b %Y')
        return edate 

    def get_name(self):
        recs = self.pool.get('project.task').search(self.cr,self.uid, [('user_id','=',self.uid)], context=self.context)
        res = self.pool.get('project.task').browse(self.cr, self.uid, recs)
        if res:
            name = res[0].user_id.name
            return name
        else:
            return      

    def get_projects(self):
        recsss = self.pool.get('project.project').search(self.cr,self.uid,['|',('user_id','=',self.uid),('members','=',self.uid)], context=self.context)
        resss = self.pool.get('project.project').browse(self.cr, self.uid, recsss)
        print resss
        return resss    

    def get_data(self,project_id):
        recs = self.pool.get('project.task').search(self.cr,self.uid, [('project_id','=',project_id.id)], context=self.context)
        res = self.pool.get('project.task').browse(self.cr, self.uid, recs)
        info = []
        for re in res:
            if re.stage_id.name == 'Done':
                today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                dtx_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                dtx_e_obj = datetime.strptime(re.date_last_stage_update,"%Y-%m-%d %H:%M:%S")
                timedelta = dtx_s_obj - dtx_e_obj
                if timedelta.days < 8:
                    last_desc = ''
                    current_desc = ''
                    hours = 0
                    for a in re.work_ids:
                        if a.user_id.id == self.uid:
                            today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                            dt_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                            dt_e_obj = datetime.strptime(a.date,"%Y-%m-%d %H:%M:%S")
                            timedelta = dt_s_obj - dt_e_obj
                            
                            if timedelta.days > 8:
                                if len(last_desc) > 0:
                                    last_desc = last_desc+','+a.name
                                else:
                                     last_desc = a.name   
                            else:
                                if len(current_desc) > 0:
                                    current_desc = current_desc+','+a.name
                                else:
                                    current_desc = a.name 
                                hours = hours + a.hours
                    data = {
                    #'project_name' : re.project_id.name,
                    'task_name' :re.name,
                    'current_desc' : current_desc,
                    'last_desc' : last_desc,
                    'description' :re.description,
                    'status' :re.stage_id.name,
                    'time' : hours
                    }
                    info.append(data)
            elif re.stage_id.name == 'Cancelled':
                today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                dtx_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                dtx_e_obj = datetime.strptime(re.date_last_stage_update,"%Y-%m-%d %H:%M:%S")
                timedelta = dtx_s_obj - dtx_e_obj
                if timedelta.days < 8:
                    last_desc = ''
                    current_desc = ''
                    hours = 0
                    for a in re.work_ids:
                        if a.user_id.id == self.uid:
                            today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                            dt_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                            dt_e_obj = datetime.strptime(a.date,"%Y-%m-%d %H:%M:%S")
                            timedelta = dt_s_obj - dt_e_obj
                            
                            if timedelta.days > 8:
                                if len(last_desc) > 0:
                                    last_desc = last_desc+','+a.name
                                else:
                                     last_desc = a.name   
                            else:
                                if len(current_desc) > 0:
                                    current_desc = current_desc+','+a.name
                                else:
                                    current_desc = a.name 
                                hours = hours + a.hours
                    data = {
                    #'project_name' : re.project_id.name,
                    'task_name' :re.name,
                    'current_desc' : current_desc,
                    'last_desc' : last_desc,
                    'description' :re.description,
                    'status' :re.stage_id.name,
                    'time' : hours
                    }
                    info.append(data)        
            else:
                last_desc = ''
                current_desc = ''
                hours = 0
                for a in re.work_ids:
                    if a.user_id.id == self.uid:
                        today_date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                        dt_s_obj = datetime.strptime(today_date,"%Y-%m-%d %H:%M:%S")
                        dt_e_obj = datetime.strptime(a.date,"%Y-%m-%d %H:%M:%S")
                        timedelta = dt_s_obj - dt_e_obj        
                        if timedelta.days > 8:
                            if len(last_desc) > 0:
                                last_desc = last_desc+','+a.name
                            else:
                                 last_desc = a.name   
                        else:
                            if len(current_desc) > 0:
                                current_desc = current_desc+','+a.name
                            else:
                                current_desc = a.name 
                            hours = hours + a.hours
                data = {
                #'project_name' : re.project_id.name,
                'task_name' :re.name,
                'current_desc' : current_desc,
                'last_desc' : last_desc,
                'description' :re.description,
                'status' :re.stage_id.name,
                'time' : hours
                }
                info.append(data)        
        return info

           

class wrapped_report_fridayrepoert(osv.AbstractModel):
    _name = 'report.latitude_report.client_status_friday_report'
    _inherit = 'report.abstract_report'
    _template = 'latitude_report.client_status_friday_report'
    _wrapped_report_class = client_status_friday_report
