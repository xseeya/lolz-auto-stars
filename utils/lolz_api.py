import aiohttp

class LolzApi:
    def __init__(self, thread_id: int, token: str) -> None:
        self.base_url = 'https://prod-api.lolz.live'
        self.thread_id = thread_id
        self.headers = {'Authorization': f'Authorization Bearer {token}'}
    
    async def get_posts(self) -> dict:
        async with aiohttp.ClientSession() as session:
            params = {'thread_id': self.thread_id, 'limit': 9999999}
            result = await session.get(url=f'{self.base_url}/posts', 
                                       headers=self.headers,
                                       params=params)
            return await result.json()
        
    async def get_post(self, post_id) -> dict:
        async with aiohttp.ClientSession() as session:
            result = await session.get(url=f'{self.base_url}/posts/{post_id}', 
                                       headers=self.headers)
            return await result.json()
        
    async def get_comments(self, post_id: int):
        async with aiohttp.ClientSession() as session:
            params = {'post_id': post_id}
            result = await session.get(url=f'{self.base_url}/posts/comments', 
                                       headers=self.headers,
                                       params=params)
            return await result.json()
        
    async def create_comment(self, post_id: int, comment_body: str) -> dict:
        async with aiohttp.ClientSession() as session:
            params = {'post_id': post_id, 'comment_body': comment_body}
            result = await session.post(url=f'{self.base_url}/posts/comments', 
                                       headers=self.headers,
                                       params=params)
            return await result.json()
        