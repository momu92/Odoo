# -*- coding: utf-8 -*- 

from odoo import models, fields

class Citas(models.Model):
    _name = "cita.cita"
    autor = fields.Char(string='Nombre Autor', required=True, help="Autor de la cita")
    cita = fields.Char(string='Cita', required=True, help="Cita")
    fecha_visualizacion = fields.Date(string="Fecha de visualizacion")
    orden_visualizacion = fields.Selection([('imp','Importante'),('pen','Pensar'),('ref','Referencias')],string="Orden de visualizacion")
