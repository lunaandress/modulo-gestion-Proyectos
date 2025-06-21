from odoo import models, fields

class Usuario(models.Model):
    _name = 'jahl_tareas.usuario'
    _description = 'Usuario del Proyecto'
    _rec_name = 'nombre'  # Este es el campo que se mostrará  el nombre de los usuarios asignados en vez del id 

    nombre = fields.Char('Nombre del Usuario', required=True)
    imagen = fields.Binary('Imagen del Usuario')
    email = fields.Char('Correo Electrónico')
    tarea_ids = fields.One2many('jahl_tareas.tarea', 'usuario_asignado', string='Tareas Asignadas')
