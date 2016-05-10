# -*- coding: utf-8 -*-
# © 2016 <AUTHOR> - <EMAIL>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Module name",
    "summary": "Module summary",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://www.tecnativa.com",
    "author": "Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # 'auto_install':False,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
    ],
    "data": [
        "security/some_model_security.xml",
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/report_name.xml",
        "views/res_partner_view.xml",
        "wizard/wizard_model_view.xml",
    ],
    "demo": [
        "demo/res_partner_demo.xml",
    ],
    "qweb": [
        "static/src/xml/module_name.xml",
    ]
}
