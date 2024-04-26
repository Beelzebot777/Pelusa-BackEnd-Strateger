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
            *- Solo disponible el puerto 443.
        
        *- Trading.
            *- Pinescript.
                *- Estrategias.
                ?- Alertas para las estrategias hechas con pinescript.
            *- Gestionador de Alertas de TradingView.
                              
    TODO- Backend 
        ?- Entorno de desarrollo:            
            - AWS EC2 como proveedor de servicios en la nube.                
                - Trader 5003. (Linux)
                    - Python
                    - Flask
                    - MySQL
                        
        !- Bases de Datos MySQL
            - Base de datos de Mercado. 
            - Base de datos de Log
            - Base de datos de Usuarios.
            - Base de datos de Alertas.            
                 
        ?- Comunicacion API's
            *- BingX
                - Datos de Mercado
                - En un futuro datos de Usuarios, tales como Operaciones y balance de Cuentas.                
            *- Binance
                - Datos de Mercado
            *- Yahoo
                - Datos de Mercado
            *- TradingView
                - Alertas.
                        
        ?- Puerto 443 Webhook
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
    
    TODO- Frontend
        ?- Entorno de desarrollo:
            - React Stockchars  - https://rrag.github.io/react-stockcharts/ - Para la visualizacion de graficos de velas.
            - yfinance          - https://pypi.org/project/yfinance/ - Para la obtencion de datos de mercado.
            - React
            - HTML
            - CSS
            - JavaScript
            - TailwindCSS       - https://tailwindcss.com/docs/guides/create-react-app - Para la implementacion con React
            - Mas tecnologias de Frontend.              
"""