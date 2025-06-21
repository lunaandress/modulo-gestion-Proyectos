from odoo import models, fields

class Proyecto(models.Model):
    _name = 'jahl_tareas.proyecto'
    _description = 'Proyecto de Gestión de Tareas'

    nombre = fields.Char('Nombre del Proyecto', required=True)
    imagen = fields.Image('Imagen del Proyecto')  # Nuevo campo de imagen
    descripcion = fields.Text('Descripción')
    usuario_ids = fields.Many2many('jahl_tareas.usuario', string='Usuario Asignado')
    tarea_ids = fields.One2many('jahl_tareas.tarea', 'proyecto_id', string='Tareas')
    
