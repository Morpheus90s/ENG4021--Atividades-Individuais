from django.shortcuts import render

def index(request):
    
   
    meu_nome = "Pedro Augusto Beserra da Silva"
    
    lista_ranking = [
        { 
            "titulo": "O Show de Truman: O Show da Vida", 
            "img": "https://admin.cnnbrasil.com.br/wp-content/uploads/sites/12/2023/07/show-de-truman.jpeg?w=1000",
            
            "links": [
                { "desc": "Ver na Netflix", "url": "https://www.netflix.com/br/title/11819086" },
                { "desc": "Trailer", "url": "https://www.youtube.com/watch?v=0-t3hIGW4jY" }
            ]
        },
        { 
            "titulo": "Jojo Rabbit", 
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTJbtJ33VTLFKJ1kzOb5VRpIRf9B6ir284zw&s",
           
            "links": [
                { "desc": "Ver no IMDb", "url": "https://www.imdb.com/pt/title/tt2584384/" }
            ]
        },
        { 
            "titulo": "Forrest Gump: O Contador de Histórias", 
            "img": "https://m.media-amazon.com/images/I/91++WV6FP4L._AC_UF894,1000_QL80_.jpg",
            "links": [
                { "desc": "Ver no IMDb", "url": "imdb.com/pt/title/tt0109830/?reasonForLanguagePrompt=browser_header_mismatch" }
            ]
        }
    ]

   
    context = {
        'nome_pagina': meu_nome,
        'ranking': lista_ranking,
    }
    
   
    return render(request, 'index.html', context)