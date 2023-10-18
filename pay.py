from selenium import webdriver
import time

# Especifica la ubicación del ejecutable de Microsoft Edge WebDriver
edge_driver_path = "driverschrome\msedgedriver.exe"

# Configura las opciones del controlador de Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True

# Inicializa el navegador Microsoft Edge con las opciones
driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)

try:
    # Abre la URL
    url = "https://www.webpay.cl/company/108464"
    driver.get(url)

    # Espera a que la página cargue completamente (puedes ajustar el tiempo de espera)
    time.sleep(5)

    # Encuentra y haz clic en el primer elemento por su ruta XPath
    xpath1 = "/html/body/tbk-main/div[2]/div/tbk-company-page/div/div/div[2]/div[2]/div/div/div"
    element1 = driver.find_element('xpath', xpath1)
    element1.click()

    # Espera a que se procese la acción antes de continuar (puedes ajustar el tiempo de espera)
    time.sleep(0.5)

    # Encuentra y haz clic en el botón "Continuar" por su ruta XPath
    xpath_continuar = "/html/body/tbk-main/div[2]/div/tbk-company-page/footer/div/div/div/button"
    element_continuar = driver.find_element('xpath', xpath_continuar)
    element_continuar.click()

    # Espera a que se procese la acción antes de continuar (puedes ajustar el tiempo de espera)
    time.sleep(0.5)

    # Encuentra el campo de correo electrónico por su ruta XPath
    xpath_email = "/html/body/tbk-main/div[2]/div/app-form-pay-page/div/div/div[2]/div/div/div[2]/div/div/div[2]/json-schema-form/form/root-widget/div/div/select-framework-widget/app-asjf-framework/div/div[1]/select-widget-widget/section-widget/div/root-widget/div[1]/div/select-framework-widget/app-asjf-framework/div/div[1]/select-widget-widget/mail-widget/div/input"
    element_email = driver.find_element('xpath', xpath_email)
    
    # Haz clic en el campo de correo electrónico
    element_email.click()
    
    # Ingresa el correo electrónico (reemplaza 'tu_correo@gmail.com' con el correo deseado)
    element_email.send_keys('tu_correo@gmail.com')

  # Encuentra el campo de monto por su ruta XPath
    xpath_monto = "/html/body/tbk-main/div[2]/div/app-form-pay-page/div/div/div[2]/div/div/div[2]/div/div/div[2]/json-schema-form/form/root-widget/div/div/select-framework-widget/app-asjf-framework/div/div[1]/select-widget-widget/section-widget/div/root-widget/div[2]/div/select-framework-widget/app-asjf-framework/div/div[1]/select-widget-widget/only-number-widget/div/input"
    element_monto = driver.find_element('xpath', xpath_monto)

  # Haz clic en el campo de monto para habilitarlo
    element_monto.click()

  # Espera a que el campo de monto esté habilitado antes de ingresar el valor
    time.sleep(1)

  # Ingresa el monto (reemplaza '1000' con el monto deseado)
    element_monto.send_keys('1000000')

    # Espera a que se habilite el botón "Pagar" (puedes ajustar el tiempo de espera)
    time.sleep(2)

     # Encuentra y haz clic en el botón "pagar" por su ruta XPath
    xpath_pagar = "/html/body/tbk-main/div[2]/div/app-form-pay-page/footer/div/div/div/button"
    element_pagar = driver.find_element('xpath', xpath_pagar)
    element_pagar.click()

except Exception as e:
    print(f"Se produjo una excepción: {e}")
    # Realiza acciones para manejar la excepción, como registrarla

# Mantén el navegador abierto hasta que el usuario lo cierre manualmente
input("Presiona Enter para cerrar el navegador...")

# Cierra el navegador manualmente al presionar
