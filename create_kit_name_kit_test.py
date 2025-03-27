import sender_stand_request
import data


def get_create_new_user_token():  # users
    response = sender_stand_request.post_create_new_user(data.user_body)
    return response.json()["authToken"]


def get_kit_name(kit_name):  # kit
   current_kit_name = data.kit_body.copy()
   current_kit_name["name"] = kit_name
   return current_kit_name

def positive_assert_201(kit_body):
    response = sender_stand_request.post_create_new_client_kit(kit_body, get_create_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_create_new_client_kit(kit_body, get_create_new_user_token())
    assert response.status_code == 400
    assert response.json()["name"] == kit_body["name"]

# Prueba 1. 201. El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_user_1_letter_in__name():# Resultado esperado 201
    current_kit_name = get_kit_name("a")# Resultado actual 201
    positive_assert_201(current_kit_name)


# Prueba 2. 201. El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test_create_user_511_letter():# Resultado esperado 201 # Resultado actual 400
    current_kit_name = get_kit_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")  # Resultado actual 400
    positive_assert_201(current_kit_name)

# Prueba 3. 400. El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_user_0_letter():#Resultado esperado 400
    current_kit_name = get_kit_name("")  # Resultado actual 201 la prueba paso
    negative_assert_400(current_kit_name)

# Prueba 4. 400.  El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_create_user_512_letter():# Resultado esperado 400 # Resultado actual 201
    current_kit_name = get_kit_name("AbbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")  # Resultado actual 400
    negative_assert_400(current_kit_name)

# Prueba 5. 201. Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_create_user_has_special_letter():#Resultado esperado 201
    current_kit_name = get_kit_name("№%@")  # Resultado actual 201 la prueba paso
    positive_assert_201(current_kit_name)

# Prueba 6. 201. Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_create_user_has_space_letter():#Resultado esperado 201
    current_kit_name = get_kit_name("A aa")  # Resultado actual 201 la prueba paso
    positive_assert_201(current_kit_name)# Actual 201

# Prueba 7. 201. Se permiten números: kit_body = { "name": "123" }
def test_create_user_has_number_letter():#Resultado esperado 201
    current_kit_name = get_kit_name("123")#Actual 201
    positive_assert_201(current_kit_name)

# Prueba 8. 400. El parámetro no se pasa en la solicitud: kit_body = { }
def test_parameter_is_not_passed_in_the_prueba():
    current_kit_name = get_kit_name( )  # Actual 201
    negative_assert_400(current_kit_name) # Error

# Prueba 9. 400.  Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_number_prueba():
    current_kit_name = get_kit_name(123)  # Esperado
    negative_assert_400(current_kit_name) #Actual