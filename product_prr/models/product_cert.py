from odoo import models, fields, api

class ProductCert(models.Model):
    _name = 'product.cert'
    _description = 'Product certification'

    specification =fields.Many2one(
        'quality.specification',
        string='Specification',
    )
    scan_plan = fields.Char(
        string='Scan plan',
        size=50,
    )
    draw_area = fields.Char(
        string='Draw area',
        size=50,
    )
    certification_type = fields.Char(
        string='Certification type',
        size=50,
    )
    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
    certifications_files = fields.Many2many(
        'ir.attachment',
        string="Attachment",
        help='You can attach the copy of your Letter'
    )
    name = fields.Selection(
        [
            ('05 - Chemical Analysis', '05 - Chemical Analysis'),
            ('07 - Quality Test Cupon', '07 - Quality Test Cupon'),
            ('10 - Tension Properties', '10 - Tension Properties'),
            ('15 - Impact Properties', '15 - Impact Properties'),
            ('20 - Hardness Testing', '20 - Hardness Testing'),
            ('23 - Heat Treat Cycle', '23 - Heat Treat Cycle'),
            ('25 - Heat Treat Charts', '25 - Heat Treat Charts'),
            ('30 - Metallographic Examination', '30 - Metallographic Examination'),
            ('35 - Visual Test', '35 - Visual Test'),
            ('40 - Penetrant Test', '40 - Penetrant Test'),
            ('45 - Magnetic Test', '45 - Magnetic Test'),
            ('50 - Ultrasonic Test', '50 - Ultrasonic Test'),
            ('53 - Volumetric Destructive Test', '53 - Volumetric Destructive Test'),
            ('55 - Radiographic Test', '55 - Radiographic Test'),
            ('57 - Volumetric Summary NDE', '57 - Volumetric Summary NDE'),
            ('60 - Dimensional Verification', '60 - Dimensional Verification'),
            ('65 - Lot Number', '65 - Lot Number'),
            ('66 - PED 2014/68/EU', '66 - PED 2014/68/EU'),
            ('67 - Certificate of Conformity', '67 - Certificate of Conformity'),
            ('68 - Request for Deviation', '68 - Request for Deviation'),
            ('69 - NACE MR0175', '69 - NACE MR0175'),
            ('70 - Hardsurfaced', '70 - Hardsurfaced'),
            ('75 - Surface Treat', '75 - Surface Treat'),
            ('76 - Surface Coating', '76 - Surface Coating'),
            ('77 - Weigth', '77 - Weigth'),
            ('78 - Traceability Marking', '78 - Traceability Marking'),
            ('83 - Welding Repair', '83 - Welding Repair'),
            ('99 - Verify Before Shipment', '99 - Verify Before Shipment'),
        ],
        string='Certification',
    )
    type = fields.Selection(
        [
            ('set', 'Set'),
            ('set (Background)', 'Set (Background)'),
            ('fund & maq', 'Fund & Maq'),
            ('fund. client', 'Fund. Client'),
            ('fund. maq.', 'Fund. maq.'),
            ('fund. PA. .', 'Fund. PA. .'),
            ('foundry & PA', 'Foundry & PA'),
            ('foundry (PA)', 'Foundry (PA)'),
            ('foundry / PA', 'Foundry / PA'),
            ('casting and Machining', 'Casting and Machining'),
            ('PA lot', 'PA lot'),
            ('machined', 'Machined'),
            ('machining / PA', 'Machining / PA'),
            ('model', 'Model'),
            ('n/a', 'N/A'),
            ('PA-Fund.', 'PA-Fund.'),
            ('PA - Model', 'PA - Model'),
            ('PA Pz Sacrifice', 'PA Pz Sacrifice'),
            ('PA only', 'PA only'),
            ('PA cast only', 'PA cast only'),
        ],
        string='Product Type',
    )
    sample_size = fields.Selection(
        [
            ('1 in 10', '1 in 10'),
            ('1 every 10 every load', '1 every 10 every load'),
            ('1 every 12', '1 every 12'),
            ('1 every 15', '1 every 15'),
            ('1 each tree', '1 each tree'),
            ('1 per laundry', '1 per laundry'),
            ('1 per master wash', '1 per master wash'),
            ('1 per day', '1 per day'),
            ('1 per lot TT', '1 per lot TT'),
            ('1 per batch TT of laundry', '1 per batch TT of laundry'),
            ('1 per batch TT per heat', '1 per batch TT per heat'),
            ('1 per order', '1 per order'),
            ('1 per piece', '1 per piece'),
            ('1 pc every 6 months', '1 pc every 6 months'),
            ('8%', '8%'),
            ('10%', '10%'),
            ('10%, minimum 3', '10%, minimum 3'),
            ('100%', '100%'),
            ('100% in Critical Areas', '100% in Critical Areas'),
            ('100% of casting surfaces', '100% of casting surfaces'),
            ('100% second SP-UT', '100% second SP-UT'),
            ('100%, Only in UT Zone', '100%, Only in UT Zone'),
            ('Eventual', 'Eventual'),
            ('Level II, AQL 1.5', 'Level II, AQL 1.5'),
            ('PA lot', 'PA lot'),
            ('Level II with 1.5 AQL', 'Level II with 1.5 AQL'),
            ('Level II with 4.0 AQL', 'Level II with 4.0 AQL'),
            ('AP Sacrifice Piece', 'AP Sacrifice Piece'),
            ('PNDG', 'PNDG'),
            ('By sending', 'By sending'),
            ('Only pre-machining area', 'Only pre-machining area'),
            ('Second PO', 'Second PO'),
            ('Second ECM Vol.', 'Second ECM Vol.'),
            ('solo pa', 'solo pa'),
            ('Foundry Only PA', 'Foundry Only PA'),
        ],
        string='Sample size',
    )