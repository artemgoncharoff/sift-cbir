# Generated by Django 2.1.8 on 2020-05-19 14:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import photologue.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBIRIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='"slug" - уникальная строка индентификатор', max_length=250, unique=True, verbose_name='slug')),
                ('name', models.CharField(max_length=250, verbose_name='Название каталога со структурами данных индекса')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('count_photos_indexed', models.PositiveIntegerField(blank=True, verbose_name='count_photos_indexed')),
                ('count_photos_for_training_from_database', models.PositiveIntegerField(blank=True, verbose_name='count_photos_for_training_from_database')),
                ('count_photos_for_training_external', models.PositiveIntegerField(blank=True, verbose_name='count_photos_for_training_external')),
                ('built', models.BooleanField(default=False, verbose_name='built')),
            ],
            options={
                'verbose_name': 'CBIRCore index',
                'verbose_name_plural': 'CBIRCore indexes',
                'ordering': ['-date_added'],
                'get_latest_by': 'date_added',
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='"slug" - уникальная строка индентификатор', max_length=250, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_file', models.FileField(blank=True, upload_to=photologue.models.get_storage_path_for_description_file_of_database, verbose_name='description_file')),
                ('count', models.PositiveIntegerField(blank=True)),
                ('cbir_index_default', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='database_default', to='photologue.CBIRIndex')),
            ],
            options={
                'verbose_name': 'database',
                'verbose_name_plural': 'databases',
                'ordering': ['-date_added'],
                'get_latest_by': 'date_added',
            },
        ),
        migrations.CreateModel(
            name='DatabasePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=photologue.models.get_storage_path_for_image, verbose_name='Фото')),
                ('date_taken', models.DateTimeField(blank=True, help_text='Date image was taken; is obtained from the image EXIF data.', null=True, verbose_name='Дата загрузки')),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('crop_from', models.CharField(blank=True, choices=[('top', 'Top'), ('right', 'Right'), ('bottom', 'Bottom'), ('left', 'Left'), ('center', 'Center (Default)')], default='center', max_length=10, verbose_name='Обрезать')),
                ('name', models.CharField(db_index=True, help_text='Name equal to corresponding filename', max_length=250, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('description_file', models.FileField(blank=True, upload_to=photologue.models.get_storage_path_for_description_file_of_database_photo, verbose_name='description_file')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.Database')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='"slug" - уникальная строка индентификатор.', max_length=250, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_file', models.FileField(blank=True, upload_to=photologue.models.get_storage_path_for_description_file_of_event, verbose_name='description_file')),
                ('status', models.CharField(choices=[('search', 'search'), ('basket', 'basket'), ('ready', 'ready')], max_length=20, verbose_name='Статус')),
                ('cbir_index', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.CBIRIndex')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.Database')),
            ],
        ),
        migrations.CreateModel(
            name='EventBasketChosenPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('database_photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.DatabasePhoto')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventBasketPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField(blank=True, null=True)),
                ('database_photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.DatabasePhoto')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=photologue.models.get_storage_path_for_image, verbose_name='Фото')),
                ('date_taken', models.DateTimeField(blank=True, help_text='Date image was taken; is obtained from the image EXIF data.', null=True, verbose_name='Дата загрузки')),
                ('view_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='view count')),
                ('crop_from', models.CharField(blank=True, choices=[('top', 'Top'), ('right', 'Right'), ('bottom', 'Bottom'), ('left', 'Left'), ('center', 'Center (Default)')], default='center', max_length=10, verbose_name='Обрезать')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_file', models.FileField(blank=True, upload_to=photologue.models.get_storage_path_for_description_file_of_event_photo, verbose_name='description_file')),
                ('is_query', models.BooleanField(default=False, verbose_name='is_query')),
                ('similarity', models.FloatField(blank=True, null=True)),
                ('database_photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.DatabasePhoto')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('transpose_method', models.CharField(blank=True, choices=[('FLIP_LEFT_RIGHT', 'Flip left to right'), ('FLIP_TOP_BOTTOM', 'Flip top to bottom'), ('ROTATE_90', 'Rotate 90 degrees counter-clockwise'), ('ROTATE_270', 'Rotate 90 degrees clockwise'), ('ROTATE_180', 'Rotate 180 degrees')], max_length=15, verbose_name='rotate or flip')),
                ('color', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a black and white image, a factor of 1.0 gives the original image.', verbose_name='color')),
                ('brightness', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a black image, a factor of 1.0 gives the original image.', verbose_name='brightness')),
                ('contrast', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a solid grey image, a factor of 1.0 gives the original image.', verbose_name='contrast')),
                ('sharpness', models.FloatField(default=1.0, help_text='A factor of 0.0 gives a blurred image, a factor of 1.0 gives the original image.', verbose_name='sharpness')),
                ('filters', models.CharField(blank=True, help_text='Chain multiple filters using the following pattern "FILTER_ONE->FILTER_TWO->FILTER_THREE". Image filters will be applied in order. The following filters are available: BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, Kernel, SHARPEN, SMOOTH, SMOOTH_MORE.', max_length=200, verbose_name='filters')),
                ('reflection_size', models.FloatField(default=0, help_text='The height of the reflection as a percentage of the orignal image. A factor of 0.0 adds no reflection, a factor of 1.0 adds a reflection equal to the height of the orignal image.', verbose_name='size')),
                ('reflection_strength', models.FloatField(default=0.6, help_text='The initial opacity of the reflection gradient.', verbose_name='strength')),
                ('background_color', models.CharField(default='#FFFFFF', help_text='The background color of the reflection gradient. Set this to match the background color of your page.', max_length=7, verbose_name='color')),
            ],
            options={
                'verbose_name': 'photo effect',
                'verbose_name_plural': 'photo effects',
            },
        ),
        migrations.CreateModel(
            name='PhotoSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Photo size name should contain only letters, numbers and underscores. Examples: "thumbnail", "display", "small", "main_page_widget".', max_length=40, unique=True, validators=[django.core.validators.RegexValidator(message='Use only plain lowercase letters (ASCII), numbers and underscores.', regex='^[a-z0-9_]+$')], verbose_name='name')),
                ('width', models.PositiveIntegerField(default=0, help_text='If width is set to "0" the image will be scaled to the supplied height.', verbose_name='width')),
                ('height', models.PositiveIntegerField(default=0, help_text='If height is set to "0" the image will be scaled to the supplied width', verbose_name='height')),
                ('quality', models.PositiveIntegerField(choices=[(30, 'Very Low'), (40, 'Low'), (50, 'Medium-Low'), (60, 'Medium'), (70, 'Medium-High'), (80, 'High'), (90, 'Very High')], default=70, help_text='JPEG image quality.', verbose_name='quality')),
                ('upscale', models.BooleanField(default=False, help_text='If selected the image will be scaled up if necessary to fit the supplied dimensions. Cropped sizes will be upscaled regardless of this setting.', verbose_name='upscale images?')),
                ('crop', models.BooleanField(default=False, help_text='If selected the image will be scaled and cropped to fit the supplied dimensions.', verbose_name='crop to fit?')),
                ('pre_cache', models.BooleanField(default=False, help_text='If selected this photo size will be pre-cached as photos are added.', verbose_name='pre-cache?')),
                ('increment_count', models.BooleanField(default=False, help_text='If selected the image\'s "view_count" will be incremented when this photo size is displayed.', verbose_name='increment view count?')),
                ('effect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_sizes', to='photologue.PhotoEffect', verbose_name='photo effect')),
            ],
            options={
                'verbose_name': 'photo size',
                'verbose_name_plural': 'photo sizes',
                'ordering': ['width', 'height'],
            },
        ),
        migrations.CreateModel(
            name='Watermark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='content/watermarks', verbose_name='image')),
                ('style', models.CharField(choices=[('tile', 'Tile'), ('scale', 'Scale')], default='scale', max_length=5, verbose_name='style')),
                ('opacity', models.FloatField(default=1, help_text='The opacity of the overlay.', verbose_name='opacity')),
            ],
            options={
                'verbose_name': 'watermark',
                'verbose_name_plural': 'watermarks',
            },
        ),
        migrations.AddField(
            model_name='photosize',
            name='watermark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_sizes', to='photologue.Watermark', verbose_name='watermark image'),
        ),
        migrations.AddField(
            model_name='eventphoto',
            name='effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventphoto_related', to='photologue.PhotoEffect', verbose_name='effect'),
        ),
        migrations.AddField(
            model_name='eventphoto',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.Event'),
        ),
        migrations.AddField(
            model_name='databasephoto',
            name='effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='databasephoto_related', to='photologue.PhotoEffect', verbose_name='effect'),
        ),
        migrations.AddField(
            model_name='cbirindex',
            name='database',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Database'),
        ),
        migrations.AlterUniqueTogether(
            name='eventphoto',
            unique_together={('event', 'database_photo', 'is_query')},
        ),
        migrations.AlterUniqueTogether(
            name='eventbasketchosenphoto',
            unique_together={('event', 'database_photo')},
        ),
        migrations.AlterUniqueTogether(
            name='databasephoto',
            unique_together={('database', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='cbirindex',
            unique_together={('database', 'name')},
        ),
    ]
