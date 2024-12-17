
import requests
import json
import os
import base64


token:str = "474371b370470a349d4b49b2fa6032f1a75ebe99f5ce59376e5f53ba2ff5fe6d3b495b4777f777f1a1fb3fc32deb52f73f394abd0299bb578d8b48f6ff6e14c08cda5a2e62e2d44f7f0d02b7e83c7256380247f2bf3df8edefc406728997d49073f9e94766d18640238bcde29edddb60bd3f8587126cc16db839f8b13879b763"

headers  = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
total_countries:list = []
base_url = "https://h45w16tt-1337.use2.devtunnels.ms"
for i in range(1,4):
    print(i)
    url:str = f"{base_url}/api/countries?pagination[page]={i}&pagination[pageSize]=100"
    request = requests.get(url,headers=headers)
    if request.status_code == 200:
        try:
            response = request.json()
            print(response)
            countries = response["data"]
            total_countries.extend(countries)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response content: {request.text}")
    else:
        print(f"Request failed with status code: {request.status_code}")
    
print(len(total_countries))
out_folder = "out"

for country in total_countries:
    
    curr_id = country["id"]
    curr_file = country["attributes"]["code"] + ".svg"
    curr_url = f"{base_url}/api/countries/{curr_id}"
    if curr_file in os.listdir(out_folder):
        with open(f"{out_folder}/{curr_file}", "r", encoding="utf-8") as file:
            svg_content:str = file.read()
            # svg_b64 = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
            country["attributes"]["icon"] = svg_content
         
            print(f"Updating {country}")
            print("------------------------------------------")
            
            response = requests.put(curr_url,headers=headers,json={"data":country["attributes"]})
            print(response)
            
            if response.status_code == 200:
                print(f"Successfully updated country {curr_id}")
            else:
                print(f"Failed to update country {curr_id} with status code: {response.status_code}")
                print(f"Response content: {response.text}")
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