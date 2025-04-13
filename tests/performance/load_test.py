from locust import HttpUser, task

class AgenticAIUser(HttpUser):
    @task
    def analyze_data(self):
        self.client.post("/analyze", json={"data": "test"})