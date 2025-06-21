from odoo import models, fields

class Etiqueta(models.Model):
    _name = 'jahl_tareas.etiqueta'
    _description = 'Etiqueta para Tareas'

    nombre = fields.Char('Nombre', required=True)
    color = fields.Integer(string="Color")

    # Relación inversa: tareas asociadas a esta etiqueta
    tarea_ids = fields.Many2many('jahl_tareas.tarea', 'tarea_etiqueta_rel', 'etiqueta_id', 'tarea_id', string='Tareas')
