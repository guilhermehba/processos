from django.shortcuts import render
from django.http import HttpResponse
from processo.models import Gerencia, Macro, Processo
from configuracoes.models import Parametro
from rest_framework import serializers




#from django.views.decorators.clickjacking import xframe_options_exempt
#from django.views.decorators.clickjacking import xframe_options_sameorigin

import json
from django.http import JsonResponse
def migrate(request, pk):

    #pk_value = obj._get_pk_val()
    all_entries = Gerencia.objects.filter(pk=pk)
    #pk = Sigtap._get_pk_val()

    data = serializers.serialize("json", all_entries, fields=('status'))

    #print(all_entries)

    return HttpResponse(data, content_type="application/json")


#@xframe_options_sameorigin
def index(request):

    gerencias=Gerencia.objects.all()

    json_array_dados = []
    json_array_processo = []
    json_array_macro = []

    for gerencia in gerencias:

        macros = Macro.objects.filter(gerencia_id=gerencia.id)

        for macro in macros:
            processos = Processo.objects.filter(macro_id=macro.id)

            for processo in processos:

                processoDados = ({
                    'id': processo.id,
                    'nome': processo.nome,
                    'descrição': processo.descricao,
                    'data': processo.data,
                    'processo': processo.processo,
                    'status': processo.status
                })

                json_array_processo.append(processoDados)

            macroDados = {
                'id': macro.id,
                'nome':macro.nome,
                'status':macro.status,
                'processo':json_array_processo
            }
            json_array_macro.append(macroDados)
            json_array_processo = []

        gerenciaDados = {
            'gerencia': {
                'id': gerencia.id,
                'nome': gerencia.nome,
                'macro': json_array_macro
            }
        }
        json_array_dados.append(gerenciaDados)
        json_array_macro = []

    parametros=Parametro.objects.get(id=1)

    return render (request, 'index.html', {'result': json_array_dados, 'parametro':parametros})
