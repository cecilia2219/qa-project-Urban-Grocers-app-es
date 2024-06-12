import configuration
import requests
import data

#funcion para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,                                                   # inserta el cuerpo de solicitud
                         headers=data.headers)                                        # inserta los encabezados

response = post_new_user(data.user_body)
#----------------------------------------------------------------------------------------------------------------------
def get_new_user_token():
    response = post_new_user(data.user_body)
    response_json = response.json()
    return response_json["authToken"]

#----------------------------------------------------------------------------------------------------------------------
#crear un nuevo kit
def post_new_client_kit(kit_body):
    auth_token = get_new_user_token()
    authorization = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer "{auth_token}'

    }

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                                                                             # inserta la dirección URL completa
                         json=kit_body,                                      # inserta el cuerpo de solicitud
                         headers=authorization)                                     # inserta los encabezado

    response = get_new_user_token()
    print(response.status_code)
    print(response.json())
#-----------------------------------------------------------------------------------------------------------------------
