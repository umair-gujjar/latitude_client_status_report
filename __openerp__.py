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
        # 'security/ir.model.access.csv',
        'templates.xml',
        'report_hotel_management_ox_report.xml',
        #'views/report_hotel_management_ox_report.xml',
        'views/departure_report.xml',
        #'wizard/hotel_oxenlab_view.xml',
    ],
}
