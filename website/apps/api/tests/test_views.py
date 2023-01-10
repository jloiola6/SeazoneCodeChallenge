from rest_framework.test import APITestCase

from apps.api.models import *


class AnuncioViewsTests(APITestCase):

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


    def test_deletar_objeto(self):
        request = self.client.delete('/anuncios/1/', {'plataforma': 'Booking'})
        self.assertAlmostEqual(request.status_code, 405)



class ReservaViewsTests(APITestCase):

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

        self.reserva = Reserva.objects.create(
                anuncio= self.anuncio,
                check_in= "2023-05-31",
                check_out= "2023-06-08",
                total= 450.0,
                comentario= "",
                qtd_hospedes= 1,
            )

    def test_editar_objeto(self):
        request = self.client.put('/reservas/1/', {'codigo': '123'})
        self.assertAlmostEqual(request.status_code, 405)


    def test_checkin_posterior_do_checkout(self):
        data = {
            "anuncio":  "/anuncios/1/",
            "check_in": "2023-07-31",
            "check_out": "2023-06-08",
            "total": 450.0,
            "comentario": "",
            "qtd_hospedes": 1
        }

        request = self.client.post('/reservas/', data, format='json')
        self.assertAlmostEqual(request.status_code, 400)
    

    def test_checkin_anterior_do_checkout(self):
        data = {
            "anuncio": "/anuncios/1/",
            "check_in": "2023-05-31",
            "check_out": "2023-06-08",
            "total": 450.0,
            "comentario": "",
            "qtd_hospedes": 1
        }

        request = self.client.post('/reservas/', data, format='json')
        self.assertAlmostEqual(request.status_code, 201)

