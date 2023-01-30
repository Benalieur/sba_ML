from django.shortcuts import render
import requests

def model(request):
    
    secteurs = [
        (00, "Indéfini"),
        (11, "Agriculture, sylviculture, pêche et chasse"),
        (21, "Extraction minière, exploitation de carrières et extraction de pétrole et de gaz"),
        (22, "Services publics"),
        (23, "Construction"),
        (31, "Fabrication"),
        (32, "Fabrication"),
        (33, "Fabrication"),
        (42, "Commerce de gros"),
        (44, "Commerce de détail"),
        (45, "Commerce de détail"),
        (48, "Transport et entreposage"),
        (49, "Transport et entreposage"),
        (51, "Information"),
        (52, "Finances et assurances"),
        (53, "Immobilier et location à bail"),
        (54, "Services professionnels, scientifiques et techniques"),
        (55, "Gestion de sociétés et d’entreprises"),
        (56, "Administration et soutien et gestion des déchets / services d’assainissement"),
        (61, "Services éducatifs"),
        (62, "Soins de santé et aide sociale"),
        (71, "Arts, divertissement et loisirs"),
        (72, "Hébergement et services alimentaires"),
        (81, "Autres services (sauf administration publique)"),
        (92, "Administration publique"),
    ]

    if request.method == 'POST':
        mois = request.POST.get('mois')
        nb_employes = request.POST.get('nb_employes')
        creation = request.POST.get('creation')
        emploi_crees = request.POST.get('emploi_crees')
        franchise = request.POST.get('franchise')
        emplacement = request.POST.get('emplacement')
        cred_renouvelable = request.POST.get('cred_renouvelable')
        petit_pret = request.POST.get('petit_pret')
        montant = request.POST.get('montant')
        secteur = request.POST.get('secteur')
        secure = request.POST.get('secure')
        data = {
            'mois': mois,
            'nb_employes': nb_employes,
            'creation': creation,
            'emploi_crees': emploi_crees,
            'franchise': franchise,
            'emplacement': emplacement,
            'cred_renouvelable': cred_renouvelable,
            'petit_pret': petit_pret,
            'montant': montant,
            'secteur': secteur,
            'secure': secure
        }

        headers = {"Content-Type": "application/json"}

        url = "http://localhost:8080/predict"

        response = requests.post(url, json=data, headers=headers)

        predictions = response.json()
        prediction = float(list(predictions['prediction'].keys())[0])
        print(predictions)

        return render(request, 'model/model_accept.html', {'prediction': prediction})

    else:
        return render(request, 'model/model.html', {'secteurs': secteurs})



def contact(request):

    return render(request, 'model/contact.html')