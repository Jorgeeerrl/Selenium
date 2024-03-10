############################################ POM (Page Object Model) #############################################

# 0- La organización de carpetas del POM se muestra en una imagen adjunta.

# 1- Es un patrón de diseño, popularmente utilizado en automatización de pruebas (Selenium).

# 2- Es una forma de separar el código de la interfaz de usuario (IU) de la lógica de la aplicación.

# 3- Se basa en crear un repositorio de objetos para elementos de UI.

# 4- Para cada página web de la aplicación que estamos automatizando, se crea una clase (o archivo de código) 
#    que contenga todos los elementos de UI y los métodos para realizar operaciones sobre esos elementos.

# 5- Es muy popular porque hace que el mantenimiento de los scrips sea más sencillo. Pe. Imaginemos que tenemos 
#    200 pruebas sobre una página en concreto. Teniendo todo sobre los elementos de esa página en una clase 
#    (archivo de código) aparte, si se cambiara cualquier cosa de algún elemento de la página, con cambiarlo 
#    en el archivo clase ya cogerían de ahí el cambio las 200 pruebas, no haría falta hacer el cambio en todas.

# 6- Favorece la reutilización de los métodos para localizar y operar objetos. Creas el método una sola vez 
#    y luego por parámetros lo vas reutilizando. Así se consigue también mucho menos código.

# 7- Código más limpio al tener operaciones y flujo (pasos que vas dando para acceder a diferentes opciones 
#    para llegar a una ventana determinada, etc), separados de las verificaciones.

# 8- El repositorio es independiente de los casos de prueba.

# 9- Los métodos obtienen nombres más reales o adecuados con lo que realmente hacen.



############################# Ejemplo de implementación: POM (Page Object Model) #############################

# Esto sería un ejemplo de archivo de clase:
# Por cada una de las páginas del sitio, crearíamos una clase como ésta.

import time
from selenium.webdriver.common.by import By
from pytest import mark
@mark.notest
base_url = "https://testautomationpractice.blogspot.com/"


class HomePage:  # aquí irían todos los elementos de la página.

    def __init__(self, driver): 
        self.driver = driver  #driver viene pasado por parámetro del constructor de la clase.
        self.wikipedia_Search = "//*[@class='wikipedia-search-input']"
        self.date_picker = "datepicker"
        self.spedd = "speed"
        self.sunday = "RESULT_Checkbox-8_0"
        self.monday = "RESULT_Checkbox-8_1"
        self.tuesday = "RESULT_Checkbox-8_2"
        self.field1 = "field1"
        self.field2 = "field2"
        self.iframe = "frame-one796456169"
        self.first_name = "RESULT_TextField-1"
        self.last_name = "RESULT_TextField-2"
        self.phone = "RESULT_TextField-3"
        self.country = "RESULT_TextField-4"
        self.city = "RESULT_TextField-5"
        self.email = "RESULT_TextField-6"
        self.gender_male = "RESULT_Radiobutton-7_0"
        self.gender_female = "RESULT_Radiobutton-7_1"
        self.submit = "FSsubmit"


# Las pruebas cogen los métodos del listado de métodos de abajo, y a su vez los métodos cogen los elementos usando 
#    los valores del listado principal. Al final, para cada uno de los elementos tenemos definido un método que
#    nos devuelve dicho elemento. Entonces nosotros cuando queremos invocar un elemento llamamos a la función 
#    del elemento correspondiente.
#    
# Así, si en la web se cambia un elemento, con solo actualizar el elemento en el listado superior, todas las 
#    funciones y pruebas relacionadas que las usen estarán actualizadas.
        

    def get_wikipedia_Search(self):
        return self.driver.find_element(By.XPATH, self.wikipedia_Search)

    def get_date_picker(self):
        return self.driver.find_element(By.ID, self.date_picker)
    
    def get_spedd(self):
        return self.driver.find_element(By.ID, self.spedd)

    def get_sunday(self):
        return self.driver.find_element(By.ID, self.sunday)

    def get_monday(self):
        return self.driver.find_element(By.ID, self.monday)

    def get_tuesday(self):
        return self.driver.find_element(By.ID, self.tuesday)

    def get_field1(self):
        return self.driver.find_element(By.ID, self.field1)

    def get_field2(self):
        return self.driver.find_element(By.ID, self.field2)

    def get_iframe(self):
        return self.driver.find_element(By.ID, self.iframe)

    def get_first_name(self):
        return self.driver.find_element(By.ID, self.first_name)

    def get_last_name(self):
        return self.driver.find_element(By.ID, self.last_name)

    def get_phone(self):
        return self.driver.find_element(By.ID, self.phone)

    def get_country(self):
        return self.driver.find_element(By.ID, self.country)

    def get_city(self):
        return self.driver.find_element(By.ID, self.city)

    def get_email(self):
        return self.driver.find_element(By.ID, self.email)

    def get_gender_male(self):
        return self.driver.find_element(By.ID, self.gender_male)

    def get_gender_female(self):
        return self.driver.find_element(By.ID, self.gender_female)

    def get_submit(self):


# También definimos funciones para realizar acciones con esos elementos.
# Como localizarlo:
              
    def get_wikipedia_Search(self):
        return self.driver.find_element(By.XPATH, self.wikipedia_Search)

    def get_date_picker(self):
        return self.driver.find_element(By.ID, self.date_picker)
    
    def get_spedd(self):
        return self.driver.find_element(By.ID, self.spedd)

    def get_sunday(self):
        return self.driver.find_element(By.ID, self.sunday)

    def get_monday(self):
        return self.driver.find_element(By.ID, self.monday)

    def get_tuesday(self):
        return self.driver.find_element(By.ID, self.tuesday)

    def get_field1(self):
        return self.driver.find_element(By.ID, self.field1)

    def get_field2(self):
        return self.driver.find_element(By.ID, self.field2)

    def get_iframe(self):
        return self.driver.find_element(By.ID, self.iframe)

    def get_first_name(self):
        return self.driver.find_element(By.ID, self.first_name)

    def get_last_name(self):
        return self.driver.find_element(By.ID, self.last_name)

    def get_phone(self):
        return self.driver.find_element(By.ID, self.phone)

    def get_country(self):
        return self.driver.find_element(By.ID, self.country)

    def get_city(self):
        return self.driver.find_element(By.ID, self.city)

    def get_email(self):
        return self.driver.find_element(By.ID, self.email)

    def get_gender_male(self):
        return self.driver.find_element(By.ID, self.gender_male)

    def get_gender_female(self):
        return self.driver.find_element(By.ID, self.gender_female)

    def get_submit(self):
        return self.driver.find_element(By.ID, self.submit)
    
# O realizar alguna acción con ese elemento:
    

    def sign_up(self, first_name, last_name, phone, country, city, email): # Función para rellenar el formulario completo.
        self.switch_to_iframe()
        self.get_first_name().send_keys(first_name)
        self.get_last_name().send_keys(last_name)
        self.get_phone().send_keys(phone) # devuelve ese elemento y luego escribe en él.
        self.get_country().send_keys(country)
        self.get_city().send_keys(city)
        self.get_email().send_keys(email)
        time.sleep(5)

    def click_sing_up(self):  # Me devuelve ese botón, y luego clickea en él.
        self.get_submit_button().click()  

    def switch_to_iframe(self):  # para cambiar al iframe y poder seleccionar los elementos de su interior.
        iframe = self.get_iframe_sign_up()
        self.driver.switch_to.frame(iframe)

    @staticmethod  # Quiere decir que pertenece a la clase, no a una instancia en particular de ella.
    def get_base_url():
        return base_url


#########################################  EJEMPLO DE TEST DE PRUEBA POM  ########################################
    
# Copiar y pegar código en otro archivo para test para realizar la prueba, según organigrama POM de la imagen. Así
# mantenemos el código de la UI separado de la lógica de la aplicación, además de darnos todas las ventajas 
# comentadas al principio.
    

def test_add_item_to_course_pack(self):
    driver=self.driver  # Crea el driver
    self.driver.get(HomePage.get_base_url())  # Accede a la url base.
    home_page = HomePage(driver)  # Instancia la clase HomePage, que sería el nombre de la clase.
    time.sleep(2)
    home_page.sign_up("Juan", "Luís", "809-999-9999", "Dom Rep.", "Sto. Domingo", "juan@mail.com") 
    # Llama a la función para rellenar el formulario pasándole los valores por parámetro.
    home_page.click_sign_up()  # Clica para enviar el formulario.

