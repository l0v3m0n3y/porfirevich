import requests
class Client():
	def __init__(self):
		self.api="https://api.porfirevich.com"
		self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
	def generate_text(self,prompt,model:str="gpt3",length:int=30):
		data={"prompt":prompt,"model":model,"length":length}
		return requests.post(f"{self.api}/generate/",json=data,headers=self.headers).json()