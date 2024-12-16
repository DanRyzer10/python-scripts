
import requests
import json
import os


token:str = "7fd157231fe0054b477fba069f8d16b39a926298536aab4113b8c229ac59d125bfe2ce78e4da2eae3d52ee740e93b92fea94a5ab81fbe4fc2683aa71d3f7c528c1fb1314c477d82bde0c02373edc5b33b3d4260bdd01c5b2e063e2654d796225f2fb14ce79578404dbdc98543773864f8ac68d3ef962ed266c16ea276e04a85a"

headers  = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
total_countries:list = []

for i in range(1,4):
    print(i)
    url:str = f"https://strapi.iss.com.ec/api/countries?pagination[page]={i}&pagination[pageSize]=100&fields[0]=name&fields[1]=code&fields[2]=number"
    request = requests.get(url,headers=headers)
    response = request.json()
    countries = response["data"]
    total_countries.extend(countries)
    
print(len(total_countries))
out_folder = "./out"
for country in total_countries:
    curr = country["attributes"]["code"] + ".svg"
    #buscar en una ruta out si existe ese archivo
    if curr in os.listdir(out_folder):
        print(f"El archivo {curr} ya existe")
        # si existe leer su contenido 
        with open(os.path.join(out_folder,curr)) as file:
            print(file.read())
        continue
    
    
    
    




# def get_countries(url:str,token:str):
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json"
#     }
#     response = requests.get(url,headers=headers)
#     return response.json()

# def main():
#     countries = get_countries(url,token)
#    # print(countries)
#     ##getone atribute
#     paises = countries["data"]
#     for pais in paises:
#         print(pais["attributes"]["code"])
#     #print(json.dumps(countries, indent=2))
    
    
# main()