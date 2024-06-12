import sender_stand_request
import data

def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body
#----------------------------------------------------------------------------------------------------------------------
#funcion positiva
def positive_assert(name):
    kit_body = get_kit_body(name)                                        # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_response = sender_stand_request.post_new_client_kit(kit_body)    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable kit_response

    assert kit_response.status_code == 201                                # Comprueba si el código de estado es 201

#---------------------------------------------------------------------------------------------------------------------
#funcion negativa
def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_negative_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_negative_response.status_code == 400
    assert kit_negative_response.json()["code"] == 400

#---------------------------------------------------------------------------------------------------------------------
#funcion sin nombre
def negative_assert_no_name(name):
    kit_body = get_kit_body(name)
    kit_negative_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_negative_response.status_code == 400
    assert kit_negative_response.json()["code"] == 400
#----------------------------------------------------------------------------------------------------------------------
#prueba 1 	El número permitido de caracteres (1)
def test_1_kit_body_1_letter_in_name_get_success_response():
    positive_assert("A")
    print("prueba 1 ")
#----------------------------------------------------------------------------------------------------------------------
#prueba 2 	El número permitido de caracteres (511)
def test_2_kit_body_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    print("prueba 2 ")
#----------------------------------------------------------------------------------------------------------------------
#prueba 3 	El número de caracteres es menor que la cantidad permitida (0)
def test_3_kit_body_0_letter_in_name_get_success_response():
    negative_assert("")
    print("prueba 3 ")
#-----------------------------------------------------------------------------------------------------------------------
#prueba 4 	El número de caracteres es mayor que la cantidad permitida (512)
def test_4_kit_body_512_letter_in_name_get_success_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    print("prueba 4 ")
#----------------------------------------------------------------------------------------------------------------------
#prueba 5 	Se permiten caracteres especiales
def test_5_kit_body_special_characters_letter_in_name_get_success_response():
    positive_assert("№%@")
    print("prueba 5 ")
#---------------------------------------------------------------------------------------------------------------------
#prueba 6 	Se permiten espacios
def test_6_kit_body_spaces_letter_in_name_get_success_response():
    positive_assert("A Aaa")
    print("prueba 6 ")
#---------------------------------------------------------------------------------------------------------------------
#prueba 7 	Se permiten números
def test_7_kit_body_numbers_in_name_get_success_response():
    positive_assert("123")
    print("prueba 7 ")
#---------------------------------------------------------------------------------------------------------------------
#prueba 8 El parámetro no se pasa en la solicitud
def test8_kit_body_name_No_name_get_success_response():
    kit_body = data.kit_body.copy()

    kit_body.pop("name")
    negative_assert_no_name(kit_body)

#----------------------------------------------------------------------------------------------------------------------
#prueba 9 Se ha pasado un tipo de parámetro diferente (número)
def test_9_kit_body_number_letter_in_name_get_success_response():
    negative_assert(123)
    print("prueba 9 ")