from odoo import models, fields

class Tarea(models.Model):
    _name = 'jahl_tareas.tarea'  # Campos simples
    _description = 'Tarea de Proyecto'
    _inherit = ['mail.thread','mail.activity.mixin']  # Corregido de 'mixi' a 'mixin'

    # Campos simples
    nombre = fields.Char('Nombre de la Tarea', required=True, tracking=True)
    descripcion = fields.Text('Descripción')
    fecha_fin = fields.Date('Fecha de Finalización', tracking=True)  # Tracking activado
    estado = fields.Selection([
        ('backlog', 'Atraso'),
        ('in_progress', 'En progreso'),
        ('to_do', 'Por hacer'),
        ('testing', 'Pruebas'),
        ('done', 'Hecho'),
    ], default='to_do', string='Estado', tracking=True)  # Tracking activado
    
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    ], string='Prioridad', default='1', tracking=True)  # Tracking activado

    # Relaciones con otros modelos
    proyecto_id = fields.Many2one('jahl_tareas.proyecto', string='Proyecto')
    usuario_asignado = fields.Many2one('jahl_tareas.usuario', string='Usuario Asignado')
    etiqueta_ids = fields.Many2many('jahl_tareas.etiqueta', string='Etiquetas', ondelete='cascade')

