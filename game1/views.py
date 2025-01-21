from django.shortcuts import render
import requests
from game1.player import Player
import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

base_url="https://api.opendota.com/api/"
# Create your views here.


def fetch_proof_from_js():
    url = "http://localhost:3000/fetch-proof"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error fetching proof from JS."

# def verify_stats(request):
#     if request.method == "GET":
#         proof = fetch_proof_from_js()
#         print(proof)
#         is_verified = True
#         if(proof == "Error fetching proof from JS."):
#             is_verified = False
#         # # Example logic: Replace this with your actual verification logic
#         # is_verified = True  # Example: You can perform checks or calculations here

#         if is_verified:
#             return JsonResponse({'message': 'Player stats are verified.'})
#         else:
#             return JsonResponse({'message': 'Verification failed. Player stats are invalid.'})
#     return JsonResponse({'message': 'Invalid request method.'}, status=405)


def players(request):
    account_id=request.GET.get('account_id')
    print(account_id)
    
    proof = fetch_proof_from_js()
    if(proof == "Error fetching proof from JS."):
        print("There was an error generating from of player Data.")
    else:
        print("Proof of player data: ", proof)
    
    specific_attr=request.GET.get('specific_attr')
    if specific_attr:
        player=Player(account_id)
        data={specific_attr:player.fetch_player_data_specific(specific_attr)}
        print(len(data[specific_attr]))
        pages=render_to_string("game1/sections/pages.html",{"total_pages":range(2,5)})
        html=render_to_string('game1/sections/matches.html',data)
        return JsonResponse({'html':html,'pages':pages})
        # return JsonResponse({'specific_attr':player.fetch_player_data_specific(specific_attr)})
    player=Player(account_id)

    return JsonResponse({'stats':player.fetch_player_data()})

# import requests




def pro_players(request):
    endpoint="proPlayers"
    response=requests.get(base_url+endpoint)
    print(response)
    # print(fetch_proof_from_js())
    # print("hello")
    return render(request, "game1/pro_players.html", {"pro_players":response.json()})

def public_matches(request):
    endpoint="publicMatches"
    response=requests.get(base_url+endpoint)
    return response

def pro_matches(request):
    endpoint="proMatches"
    response=requests.get(base_url+endpoint)
    return response

def index(request):
    return render(request, "game1/index.html")

# def fetch_proof_from_js():
#     url = "http://localhost:3000/fetch-proof"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return "Error fetching proof from JS."

# def verify_stats(request):
#     if request.method == "GET":
#         proof = fetch_proof_from_js()
#         print(proof)
#         is_verified = True
#         if(proof == "Error fetching proof from JS."):
#             is_verified = False
#         # # Example logic: Replace this with your actual verification logic
#         # is_verified = True  # Example: You can perform checks or calculations here

#         if is_verified:
#             return JsonResponse({'message': 'Player stats are verified.'})
#         else:
#             return JsonResponse({'message': 'Verification failed. Player stats are invalid.'})
#     return JsonResponse({'message': 'Invalid request method.'}, status=405)