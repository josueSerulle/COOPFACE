# Generated by Django 4.0.3 on 2022-07-03 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(null=True)),
                ('monto_solicitado', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('cuotas', models.IntegerField(null=True)),
                ('observacion', models.TextField(null=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='LoanTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('interes_mensual', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=13)),
                ('celular', models.CharField(max_length=11)),
                ('telefono', models.CharField(max_length=11)),
                ('correo', models.CharField(max_length=50)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PersonTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SavingTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
                ('estado', models.IntegerField(default=1)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.personmodel')),
            ],
        ),
        migrations.CreateModel(
            name='SavingTransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('tipo_transaccion', models.BooleanField(null=True)),
                ('estado', models.IntegerField(default=1)),
                ('id_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.partnermodel')),
                ('id_tipo_ahorro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.savingtypemodel')),
            ],
        ),
        migrations.AddField(
            model_name='personmodel',
            name='id_tipo_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.persontypemodel'),
        ),
        migrations.CreateModel(
            name='PersonJobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('direccion', models.CharField(max_length=255)),
                ('estado', models.IntegerField(default=1)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.personmodel')),
            ],
        ),
        migrations.CreateModel(
            name='PersonAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('estado', models.IntegerField(default=1)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.personmodel')),
            ],
        ),
        migrations.AddField(
            model_name='partnermodel',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.personmodel'),
        ),
        migrations.CreateModel(
            name='LoanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(null=True)),
                ('fecha_vencimiento', models.DateField(null=True)),
                ('monto_prestamo', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('cuotas', models.IntegerField(null=True)),
                ('interes', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('observacion', models.TextField(null=True)),
                ('estado', models.IntegerField(default=1)),
                ('id_garannte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.personmodel')),
                ('id_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.partnermodel')),
                ('id_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.loanapplicationmodel')),
                ('id_tipo_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.loantypemodel')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.usersmodel')),
            ],
        ),
        migrations.CreateModel(
            name='LoanInstallmentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_expiracion', models.DateField(null=True)),
                ('no_cuota', models.IntegerField(null=True)),
                ('capital', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('interes', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('atraso', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('pago_capital', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('pago_interes', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('pago_atraso', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('estado', models.IntegerField(default=1)),
                ('id_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.loanmodel')),
            ],
        ),
        migrations.AddField(
            model_name='loanapplicationmodel',
            name='id_garannte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.personmodel'),
        ),
        migrations.AddField(
            model_name='loanapplicationmodel',
            name='id_socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.partnermodel'),
        ),
        migrations.AddField(
            model_name='loanapplicationmodel',
            name='id_tipo_prestamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.loantypemodel'),
        ),
        migrations.AddField(
            model_name='loanapplicationmodel',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coopVirtual.usersmodel'),
        ),
    ]
