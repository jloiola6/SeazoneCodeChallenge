from django.test import TestCase
from apps.api.models import *


class AnuncioTestCase(TestCase):

    def setUp(self):
        self.imovel = Imovel.objects.create(
                codigo= 20230001,
                limite_hospedes= 3,
                qtd_banheiros= 1,
                aceita_animais= 1,
                valor_limpeza= 56.85,
                data_ativacao= "2023-01-09"
            )

        self.anuncio= Anuncio.objects.create(
                imovel= self.imovel,
                plataforma= "AirBnb",
                taxa_plataforma= 3.0
            )


    def test_codigo_aleatorio(self):
        reserva = Reserva.objects.create(
                anuncio= self.anuncio,
                check_in= "2023-05-31",
                check_out= "2023-06-08",
                total= 450.0,
                comentario= "",
                qtd_hospedes= 1,
            )
        self.assertEqual(len(str(reserva.codigo)), 15)
    

