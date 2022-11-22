from django.db import models
from django_mirror.widgets import MirrorArea
from codemirror import CodeMirrorTextarea

codemirror_widget = CodeMirrorTextarea(
    mode="python",
    theme="cobalt",
    config={
        'fixedGutter': True
    },
)

# Create your models here.
class Question(models.Model):
    """
    This class represents a practice question for the web application.
    It will be stored as a multi-line string with indents, and
    displayed inside of a code editor.
    """
    question_code = models.TextField(
        widget=codemirror_widget
    )