from application import init_app

app = init_app()


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)
