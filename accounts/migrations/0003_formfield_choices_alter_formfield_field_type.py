# Generated by Django 5.1.3 on 2024-11-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_formfield_field_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='choices',
            field=models.TextField(blank=True, help_text='Comma-separated options for multiple checkboxes', null=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('text', 'Text'), ('date', 'Date'), ('number', 'Number'), ('checkbox', 'Checkbox'), ('multiple_checkbox', 'Multiple Checkbox')], max_length=50),
        ),
    ]