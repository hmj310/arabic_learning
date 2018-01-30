# Generated by Django 2.0.1 on 2018-01-26 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArabicVerb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_meaning', models.CharField(max_length=10)),
                ('pronunciation', models.CharField(max_length=10)),
                ('arabic_spelling', models.CharField(max_length=10)),
                ('conjugated_form', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Infinitive_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_meaning', models.CharField(max_length=10)),
                ('infinitive_form', models.CharField(max_length=10)),
                ('pronunciation', models.CharField(max_length=10)),
                ('arabic_spelling', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pronoun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pronoun', models.CharField(max_length=10)),
                ('pronunciation', models.CharField(max_length=10)),
                ('arabic_spelling', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='arabicverb',
            name='infinitive_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arabic.Infinitive_form'),
        ),
        migrations.AddField(
            model_name='arabicverb',
            name='mood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arabic.Mood'),
        ),
        migrations.AddField(
            model_name='arabicverb',
            name='pronoun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arabic.Pronoun'),
        ),
    ]
