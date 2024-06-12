import httpx
from prefect import task, flow, get_run_logger
from time import sleep
import asyncio

# API_KEY = "sua_chave_api"
BASE_URL = "https://rickandmortyapi.com/api"


class CustomRequestException(Exception):
    pass


attempt_count = 0


@task(
    retries=3,
    retry_delay_seconds=2,
    timeout_seconds=1,
)
def get_all_character_data():
    global attempt_count
    logger = get_run_logger()
    try:
        attempt_count += 1
        if attempt_count == 1:
            sleep(2)
        url = f"{BASE_URL}/character"
        api_response = httpx.get(url, verify=False)
        api_response.raise_for_status()
        logger.info("Fetched all character data successfully 🤓:")
        return api_response.json()
    except asyncio.CancelledError as e:
        custom_message = (
            "Error: Task get_all_character_data "
            "was cancelled due to timeout"
        )
        logger.error(custom_message)
        raise CustomRequestException(custom_message) from e


@task(
    retries=3,
    retry_delay_seconds=2,
)
def get_all_episode_data():
    logger = get_run_logger()
    try:
        url = f"{BASE_URL}/episode"
        api_response = httpx.get(url, verify=False)
        api_response.raise_for_status()
        logger.info("Fetched all episode data successfully 🤓:")
        return api_response.json()
    except asyncio.CancelledError as e:
        custom_message = (
            "Error: Task get_all_episode_data "
            "was cancelled due to timeout"
        )
        logger.error(custom_message)
        raise CustomRequestException(custom_message) from e


@flow
def rick_and_morty_data():
    logger = get_run_logger()
    try:
        get_all_character_data()
    except CustomRequestException as e:
        logger.error(f"get_all_character_data failed after retries: {e}")

    try:
        get_all_episode_data()
    except CustomRequestException as e:
        logger.error(f"get_all_episode_data failed after retries: {e}")


if __name__ == "__main__":
    rick_and_morty_data()
