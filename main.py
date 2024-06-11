import httpx
from prefect import task, flow, get_run_logger
from httpx import TimeoutException
from time import sleep

API_KEY = "sua_chave_api"
BASE_URL = "https://rickandmortyapi.com/api"


@task
def get_all_character_data():
    try:
        url = f"{BASE_URL}/character"
        sleep(2)
        api_response = httpx.get(url, verify=False, timeout=5)
        api_response.raise_for_status()
        logger = get_run_logger()
        logger.info("Fetched all character data successfully 🤓:")
        return api_response.json()
    except httpx.RequestError as e:
        logger = get_run_logger()
        logger.error(f"Failed to fetch all character data: {str(e)}")
        raise


@task
def get_single_character_data(id: int):
    try:
        url = f"{BASE_URL}/character/{id}"
        api_response = httpx.get(url, verify=False)
        api_response.raise_for_status()
        logger = get_run_logger()
        logger.info("Fetched all character data successfully 🤓:")
        return api_response.json()
    except httpx.RequestError as e:
        logger = get_run_logger()
        logger.error(f"Failed to fetch all character data: {str(e)}")
        raise


@flow(retries=3, retry_delay_seconds=2, timeout_seconds=1)
def single_character_data():
    final_state = get_all_character_data.submit().wait(0.1)
    logger = get_run_logger()
    if final_state:
        logger.info("The task is done")

    else:
        logger.info("The task is canceled because it takes too long to run")


if __name__ == "__main__":
    single_character_data()
