import requests
class Base():
    def method_post(self,url,params = None,data = None,headers = None,files = None):
        return requests.post(url = url,params = params,data = data,headers = headers,files = files)
    def method_get(self,url,params = None,data = None,headers = None,files = None):
        return requests.get(url = url,params = params,data = data,headers = headers,files = files)
    def method_put(self,url,params = None,data = None,headers = None,files = None):
        return requests.put(url = url,params = params,data = data,headers = headers,files = files)
    def method_delete(self,url,params = None,data = None,headers = None,files = None):
        return requests.delete(url = url,params = params,data = data,headers = headers,files = files)

    def requests_type(self,method,url,params = None,data = None,headers = None,files = None):
        if method =='post' or method =='POST':
            return self.method_post(url = url,params = params,data = data,headers = headers,files = files)
        elif method =='get' or method =='GET':
            return self.method_get(url = url,params = params,data = data,headers = headers,files = files)
        elif method =='put' or method =='PUT':
            return requests.put(url = url,params = params,data = data,headers = headers,files = files)
        elif method =='delete' or method =='DELETE':
            return requests.delete(url = url,params = params,data = data,headers = headers,files = files)




