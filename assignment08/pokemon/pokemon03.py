from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

async def get_pokemon(client, url):
    start_time = time.perf_counter()
    print(f"{time.ctime()} - Fetching data from {url}")
    resp = await client.get(url)
    pokemon = resp.json()
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    print(f"{time.ctime()} - Fetched data from {url} in {duration:.2f} seconds")
    
    return Pokemon(pokemon)

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list = [random.randint(1, 151) for _ in range(5)]

        for number in rand_list:
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(client, url)))

        pokemons = await asyncio.gather(*tasks)
        return pokemons

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    asyncio.run(index())
