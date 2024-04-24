"""
*   El nombre del proyecto es 'Trader @Pelusa'.
*   'Trader @Pelusa' es un proyecto de software.
*   'El objetivo de Trader @Pelusa' es suministrar asistencia en linea (2 segundos de delay) al trader.
*   El desarrollo de 'Trader @Pelusa' contempla el uso de herramientas tales como:
*       React, Python, Pinescript, TradingView Webooks, BingXApi y BingXData.
        
*   'Pelusa' En tanto a espectativas de futuro espera ser un ayudante absoluto en el 
*        Trading, utilizando tecnologias de IA, deeplearning y bigdata.
*   'Pelusa' en un futuro podria requerir del uso de otras herramientas y tecnologias.

!Descripcion por temas de pelusa:
    TODO- TradingView.
        ?- Webhook.
            *- Solo disponible el puerto 80 y 443.
        
        *- Trading.
            *- Pinescript.
                *- Estrategias.
                ?- Alertas para las estrategias hechas con pinescript.
            *- Gestionador de Alertas de TradingView.
        *- Datos.                        
            ?- Reportes.
            ?- Mediante Scraping.     
                              
    TODO- Backend 
        ?- Entorno de desarrollo:
            - Flask (Python)
            
        !- Base de Datos MySQL
            - Datos de mercado
            - Datos de cuentas                        
                - Datos de Trading
                - Datos Operaciones
                 
        ?- Comunicacion API's
            *- BingX
            *- Binance
            *- Yahoo
            *- TradingView
                        
        ?- Puerto 80 Webhook
            - Recibir Alertas de TradingView.
            - Procesa las Alertas recibidas.            
            - Enviar Alertas_Procesadas a Frontend.
    
        ?- Puerto 5000        
            TODO - Frontend      
              
        ?- Reportes.    
                            
    TODO - API
        *- BingX 
            *- Informacion de mercado
            *- Informacion de Trading  
                *- Estado Actual Operaciones.
            *- Trading                    
                *- Operar Futuros 'Perpetual Futures':                        
                    *- Abrir Orden:                   
                    *- Modificar Orden
                    *- Cancelar Orden
                    *- Cancelar Todas las Ordenes                                                                                                            
            *- Estado Actual Cuentas:
                *- Futuros                        
                *- Spot                                  
        *- Binance
            *- Informacion de mercado
        *- Yahoo
            *- Informacion de mercado       
        *- TradingView
            *- Webhook - Alertas
            *- ????????????????
    
    TODO- Frontend
        ?- Entorno de desarrollo:
            - React Stockchars - https://rrag.github.io/react-stockcharts/ - Para la visualizacion de graficos de velas.
            - yfinance - https://pypi.org/project/yfinance/ - Para la obtencion de datos de mercado.
            - React
            - HTML
            - CSS
            - JavaScript
            - TailwindCSS - https://tailwindcss.com/docs/guides/create-react-app - Para la implementacion con React
            - Mas tecnologias de Frontend.              
"""


"""
# Software Requirements Document

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Requerimientos Funcionales:    
    - Visualizar graficos como en TradingView.
    - Recibir alertas de TradingView.
    - Procesar alertas de TradingView.
    - Enviar alertas procesadas a Frontend.
    - Abrir, Modificar, Cancelar Ordenes de Trading.
    - Cancelar todas las ordenes de Trading.
    - Ver estado actual de las cuentas de Trading.    
    - Ver estado actual de las operaciones de Trading.
    - Ver informacion de mercado.
    - Generacion de Reportes.    

Requerimientos No funcionales:
    - Seleccionar un patrones de diseño de software.
    - Buen codigo.
    - Buena estructura de carpetas.
    - Codigo que se entienda por si solo y que sea facil de entender por otro programador.
    - Modularidad.
    - A ser posible escalabilidad.    
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

!Escalabilidad y Carga:
!       ¿Cuántos usuarios esperas atender simultáneamente?
            Durante el primer año entre 2.
            Apartir del segundo año el sistema debe ser capaz de atender a 100 usuarios simultaneamente.

!       ¿Qué volumen de datos se espera manejar, y con qué frecuencia se accederá o actualizará esta información?

            -------------------------------------- Volumen de datos del mercado-------------------------------------

            Ejemplo de Estimacion del volumen de datos.            
            A bingX cada 1 segundo, para rellenar los datos de mercado. Inicialmente solo accederemos a la grafica de bitcoin. 
            Rellenando graficamente las temporalidades de 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w, 1m, 1y. 
            
            Ejemplo de Volumen de datos con Bitcoin en velas de 1m, en 15 años:
                - 118 megas en total
            Ejemplo de Volumen de datos con Bitcoin en velas de 5m, en 15 años:
                - 23 megas en total
            Ejemplo de Volumen de datos con Bitcoin en velas de 15m, en 15 años:
                - 8 megas en total                
            Ejemplo de Volumen de datos con Bitcoin en velas de 30m, en 15 años:
                - 4 megas en total
            Ejemplo de Volumen de datos con Bitcoin en velas de 1h, en 15 años:
                - 2 megas en total
            Ejemplo de Volumen de datos con Bitcoin en velas de 4h, en 15 años:
                - 500 kilos en total
            Ejemplo de Volumen de datos con Bitcoin en velas de 1d, en 15 años:
                - 100 kilos en total
            Ejemplo de Volumen de datos con Bitcoin en velas de 1w, en 15 años:
                - 20 kilos en total
            Ejemplo de Volumen de datos con Bitcoin en velas de 1Y, en 15 años:
                - 4 kilos en total
            
            En total tenemos: 160 megas en total.
            
            ---------------------------------------- Frecuencia de actualizacion del mercado------------------------------------------------------------
            Camino de ida:      El frontend - Backend - Bing X.
            Camino de vuelta:   Bing X - Backend - Frontend.
                        
            La frecuencia de actualizacion de los datos sera de 1 segundo, para la vela actual. Desde el backend a bingX.
            La frecuencia de las velas anteriores a la actual, es de 1 vez por temporalidad. Desde el backend a bingX y desde el backend al frontend.
                                                        

            Los siguientes volumenes de datos y frecuencias son irrelevantes devido a su tamaño. Despreciables al 10%.
            - Volumen de datos de las alertas de TradingView
            - Frecuencia de actualizacion de los datos de alertas de TradingView
            - Volumen de datos de las Cuentas
            - Frecuencia de actualizacion de los datos de alertas de TradingView
                    
*   Consistencia y Disponibilidad:
*       ¿Qué nivel de consistencia es necesario para los datos? (por ejemplo, consistencia fuerte, eventual, etc.)
            El objetivo de futuro es conseguir una consistencia fuerte.
            Inicialmente y al tratarse de un entorno de pruebas, se espera que la consistencia sea eventual.
                                    
*       Fallo y Tolerancia a fallos de Trader @Pelusa:
            En tanto a la tolerancia a fallos, el sistema cuenta con una forma manual de operacion, en caso de que el sistema falle. La 
            forma manual de operacion se hace directamente desde la plataforma de BingX. https://bingx.com/. 
            Inicialmente se espera que el sistema falle, por lo que se espera que el sistema sea robusto y tolerante a fallos a medida que se vaya actualizando.
            La robuztes del sistema se evaluara al final de cada ciclo de desarrollo. 

*       Fallo y Tolerancia a fallos del Servidor:
            Objetivo de disponibilidad del 99.9%. (24/7/365)
            Objetivo de tolerancia a fallos del 99.9%. (24/7/365)            
            Esto se negocia con AWS, el proveedor de servicios en la nube.
           
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
                
?   Interacciones entre servicios:
?       ¿El sistema se basará en una arquitectura de microservicios, servicios monolíticos, o una mezcla de ambos?
            Arquitectura de Microservicios. Para una aplicacion de Trading la mejor arquitectura es la de microservicios.

        
?       ¿Cómo se comunicarán los componentes del sistema entre sí? (sincronía, asincronía, colas de mensajes, etc.)
            En su mayoria asincronia.

TODO    Seguridad y Compliance:
TODO        ¿Existen requisitos específicos de seguridad o cumplimiento normativo que deben ser considerados en la arquitectura?
                Durante la etapa inical de desarrollo no se considera necesario cumplir con normativas de seguridad.
                Sin embargo se deben estudiar las problematicas de tener el puerto 80 abierto, y como se puede mitigar los riesgos de seguridad.
        
!       Infraestructura y Entorno de despliegue:
!           ¿Dónde se alojará el backend (en la nube, en servidores locales, híbrido)?
                En la nube, en AWS.
!           ¿Qué tecnologías y herramientas de infraestructura ya están en uso o se planifican utilizar?
                No se ha definido.

*      Usuarios y Roles
*          ¿Quiénes son los usuarios finales del sistema?
                El software es de uso personal o privado. 
*          ¿Qué roles específicos existirán dentro del sistema? Por ejemplo, administradores, traders regulares, analistas, etc.
                Solo un rol, el de usuario final.
*          ¿Cuáles son las capacidades y restricciones de cada rol?
                El usuario final podra:
                - ver la informacion de mercado.
                - dibujar sobre los graficos.
                - operar, 
                - ver el estado de las cuentas y operaciones.
                - ver los reportes generados por el sistema. 
                - Crear, modificar y recibir alertas de trading.

?       Funcionalidades Detalladas
?          ¿Qué funcionalidades específicas para los usuarios en cada operación de trading?
                - Abrir, Modificar, Cancelar ordenes en BingX.
?          ¿Cuáles son los requisitos para operar en BingX?
                - Para abrir una operacion se necesita:
                    - El Ticker del mercado.
                    - El tipo de operacion (Long o Short).
                    - El Apalancamiento.
                    - El tamaño de la operacion (cantidad de dinero a invertir [Margen]).
                    - Opcionales:
                        - Stop Loss.
                        - Take Profit.
                - Para cerrar una operacion se necesita:
                    - El ID de la operacion.                    
                - Para modificar una operacion se necesita:
                    - El ID de la operacion.                                        
                    - Nuevo Stop Loss y/o Nuevo Take Profit.                    
?          ¿Cómo deben gestionarse las notificaciones y alertas dentro de la aplicación?
                - Alertas generadas por TradingView.
                - Alertas generadas por el sistema.                
?          ¿Cuáles son los requisitos específicos para los reportes y qué datos deben incluirse?
                - Los inputs para extraer los reportes deben ser:
                    - Rango de tiempo.
                    - Long, Short o ambas.
                    - Ticker o Tickers.
                    - Sectores o Indices.
                    - Tipo de estrategia o sin estrategia.

TODO    Interfaz y Experiencia de Usuario
TODO        ¿Cuáles son los requisitos iniciales específicos de la interfaz de usuario?
                - Con respecto de la visualizacion de graficos:                
                    - Grafico de velas, cuyos inputs sean:
                        - Ticker.
                        - Temporalidad.
                    - La data para rellenar el grafico de velas se obtendra de la API de BingX, yfinance o Binance.                                    
                - Se necesita dibujar sobre el grafico de velas. (Lineas y texto (labels))
            Cuales son los requisitos futuros en la interfaz de usuario?
                - Posibilidad de realizar ordenes, mediante un frame con los inputs necesarios. (Inspirarse en TradingView)
                - Dibujar o indicar las alertas tanto de tradingView como del propio sistema.
                - Posibilidad de realizar ordenes basandonos en las alertas.
TODO        ¿Existen requisitos para la compatibilidad con dispositivos móviles o diferentes navegadores?
                - El desarrollo responsive sera tratado en un futuro, en la etapa inicial del proyecto lo que se busca es la funcionalidad.

!       Integración y Compatibilidad
!           ¿Cómo se integrarán los diversos servicios externos y APIs?
                - Integracion TradingView:
                    - Weebhook en TradingView.
                    - Recepcion de datos mediante Puerto 80 o 443 en Flask.
                - Integracion BingX API:
                    - Autentificacion
                    - Envio o Recepcion de datos desde BingX.
                - Integracion Binance API:
                    - Envio de datos desde BInance.    
                - Integracion Yfinance API:
                    - Envio de datos Yfinance.
!           ¿Qué protocolos de comunicación se utilizarán para garantizar la compatibilidad entre diferentes servicios y componentes?
                - Se utilizara en su mayoria el protocolo HTTP, utilizando el puerto 80. 
                - En un futuro se espera utilizar HTTPS, utilizando el puerto 443.
                
*       Rendimiento y Escalabilidad
*           ¿Cuáles son los objetivos específicos de rendimiento para las operaciones de trading en tiempo real?
                - Las especificaciones de rendimiento vienen delimitadas por las diferentes APIS.
                    - BingX:
                        Grupo de API sobre consulta de datos del Mercado:
                            - Límite Total de IP: El límite total para todas las interfaces dentro de este grupo es de 100 solicitudes por cada 10 segundos. 
                            Esto significa que, sumando todas las solicitudes a las diferentes interfaces de este grupo, no deberías exceder las 100 solicitudes en 10 segundos.
                        Grupo de API de Cuenta, operaciones y consultas sobre cuenta:
                            - Límite Total de IP: El límite total es de 1000 solicitudes cada 10 segundos para todas las interfaces en este grupo.
                            - Límite Individual de IP: Cada interfaz tiene un límite individual de 100 solicitudes por cada 10 segundos. 
                            Es decir, puedes hacer hasta 100 solicitudes a una sola interfaz específica dentro de este grupo, sin exceder el límite total de 1000 solicitudes.

*           ¿Cómo se manejará el crecimiento en el volumen transacciones en el tiempo?
                - La principal limitacion viene dada por BingX, el exchange que utilizaremos para operar. Las restricciones en tanto a las 
                transacciones viene dado por: https://bingx-api.github.io/docs/#/en-us/swapV2/base-info.html#Rate%20limit .
*           ¿Qué estrategias de escalado horizontal o vertical están planificadas?
                - Inicio con una Instancia de AWS: En la fase inicial, utilizaremos una instancia única de AWS que alojará el FrontEnd, Backend y la Base de Datos. 
                    Esta configuración simplifica el despliegue inicial y la gestión mientras el tráfico y las cargas son relativamente bajos.
                Introducción de Docker para Optimización: A medida que el sistema crezca, planeamos implementar Docker para contenerizar y separar las aplicaciones del 
                    FrontEnd, Backend y la Base de Datos en contenedores individuales. Esto no solo mejorará la gestión y el despliegue de las aplicaciones, sino que 
                    también optimizará el uso de los recursos dentro de la instancia de AWS. Esta etapa representa una optimización y modularización más que un escalado vertical per se.
                Escalado Horizontal con Kubernetes: Para manejar un aumento significativo en la carga y las solicitudes, implementaremos Kubernetes para orquestar 
                    el escalado horizontal de los contenedores. Kubernetes facilitará la adición de más instancias de contenedores distribuidos a través de múltiples 
                    máquinas (nodos) según sea necesario, asegurando alta disponibilidad y escalabilidad.

?       Seguridad y Privacidad
?           ¿Cuáles son las consideraciones específicas de seguridad para proteger la información financiera y personal de los usuarios?
                - Inicialmente mientras el proyecto permanezca privado:    
                    - Medidas de seguridad minimas:
                        
                
                - En un futuro cuando el proyecto sea no solo de uso privado:
                    - Cumplir regulaciones: GDPR y HIPAA.
?           ¿Qué medidas de seguridad y cifrado se implementarán?
?           ¿Existen requisitos de cumplimiento normativo relevantes para la región o sector específico, como GDPR o HIPAA?

TODO    Mantenimiento y Soporte
TODO        ¿Cómo se realizará el mantenimiento del sistema?
TODO        ¿Qué niveles de soporte técnico se ofrecerán a los usuarios?
TODO        ¿Cómo se gestionarán las actualizaciones y parches del sistema?

!       Pruebas
!           ¿Qué estrategias de pruebas se implementarán para asegurar la funcionalidad y la fiabilidad del sistema?
!           ¿Cómo se validarán las integraciones con servicios externos?
!           ¿Cuáles son los criterios para las pruebas de aceptación del usuario?

*       Despliegue y Operaciones
*           ¿Cómo y dónde se desplegará el sistema?
*           ¿Qué procesos se utilizarán para el despliegue continuo y la integración continua?
*           ¿Cuáles son los planes de recuperación ante desastres y continuidad del negocio?


------------------------
Los pasos a produccion por version  de 1 decimal.
Cada version deberia corresponder con un prototipo operativo.
cada prototipo, es operativo cuando:
- se han escrito los test scripts y se han aceptado
- Estos se han ejecutado
- Los script son aceptados y autorizados
- el procedimento de paso produccion esta escrito y probado
- se ejecuta el procedimiento de paso a produccion
quiza lo has hecho pero con el nombre de Go Live
------------------------       

"""


