from django.db import models

from random import randint


class Imovel(models.Model):
    ACEITA_ANIMAIS_CHOICES = (
        (1, "Sim"),
        (0, "Não"),
        
    )

    codigo = models.IntegerField()
    limite_hospedes = models.IntegerField()
    qtd_banheiros = models.IntegerField()
    aceita_animais = models.IntegerField(choices=ACEITA_ANIMAIS_CHOICES)
    valor_limpeza = models.FloatField()
    data_ativacao = models.DateField(null= True)

    criacao = models.DateTimeField('Criado em', auto_now_add= True)
    ultima_atualizacao = models.DateTimeField('Atualizado em', auto_now= True)

    def __str__(self):
        return str(self.codigo)
    

class Anuncio(models.Model):
    PLATAFORMAS_CHOICES = (
        ("AirBnb", "AirBnb"),
        ("Zap Imóveis", "Zap Imóveis"),
        ("Booking", "Booking"),
    )

    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='anuncios')
    plataforma = models.CharField(max_length=50, choices=PLATAFORMAS_CHOICES, blank=False, null=False)
    taxa_plataforma = models.FloatField()

    criacao = models.DateTimeField('Criado em', auto_now_add= True)
    ultima_atualizacao = models.DateTimeField('Atualizado em', auto_now= True)

    def __str__(self):
        return f'{self.imovel} - {self.plataforma} - {self.taxa_plataforma}'


class Reserva(models.Model):
    codigo = models.IntegerField()
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='reservas')
    check_in = models.DateField()
    check_out = models.DateField()
    total = models.FloatField()
    comentario = models.TextField(blank=True, null=True)
    qtd_hospedes = models.IntegerField()

    criacao = models.DateTimeField('Criado em', auto_now_add= True)
    ultima_atualizacao = models.DateTimeField('Atualizado em', auto_now= True)

    def save(self, *args, **kwargs):
        parametro = False
        while not parametro:
            codigo = ''
            for x in range(15):
                codigo += str(randint(1, 9))
            
            if not Reserva.objects.filter(codigo= codigo).exists():
                parametro = True

        self.codigo = int(codigo)
        super(Reserva, self).save(*args, **kwargs)