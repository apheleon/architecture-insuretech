from locust import HttpUser, between, task
import os

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://test-app-service"
    
    @task
    def index(self):
        self.client.get("/")
    
    @task(2)
    def metrics(self):
        self.client.get("/metrics")