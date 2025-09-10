from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"message": "Medical service is healthy"}


def main():
    print("Hello from medical!")


if __name__ == "__main__":
    main()
