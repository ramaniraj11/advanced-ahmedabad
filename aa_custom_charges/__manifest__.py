{
    'name': 'Advanced Ahmedabad custom changes',
    'category': 'Sale',
    'summary': 'Advanced Ahmedabad custom changes',
    'description': """Advanced Ahmedabad custom changes.""",
    'version': '18.0.0.0.0',
    'depends': ['sale_management', 'purchase'],
    "data": [
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/product_template_form_view.xml',
        'data/ir_sequence_data.xml',
        'report/ir_actions_report.xml',
        'report/ir_actions_report_templates.xml',
        'report/purchase_quotation_templates.xml',
        'report/purchase_reports.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
