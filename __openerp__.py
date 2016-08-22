# -*- coding: utf-8 -*-
{
    'name': "Latitude Client Status Monday Report",

    'summary': "Clients projects and task report",

    'description': "projects and task report",

    'author': "Tax Tech",
    'website': "http://www.taxtech.com",


    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        
        'templates.xml',
        'report_client_status_ox_report.xml',
        'views/client_status_report.xml',
        
    ],
}
