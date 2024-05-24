import asyncio
from loguru import logger

async def log_server_status():
    while True:
        # Aquí puedes añadir cualquier lógica para verificar el estado del servidor
        logger.info("Server is running smoothly")
        await asyncio.sleep(60)  # Espera 60 segundos antes de registrar el estado de nuevo
