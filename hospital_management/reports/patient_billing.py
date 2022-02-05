from odoo import api, models, _


# How To Call A Python Function While Printing PDF Report in Odoo
# https://www.youtube.com/watch?v=JGWc1KjyIBk&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=62
class PatientBillingReport(models.AbstractModel):
    _name = 'report.hospital_management.report_patient_billing_details'
    _description = 'Patient Billing Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['patient.billing'].browse(docids[0])
        billing_lines = self.env['patient.billing.line'].search('name', '=', docids[0])
        bills = []
        bills = billing_lines

        return {
            'doc_model': 'patient',
            'docs': docs,
            'bills':bills


        }
