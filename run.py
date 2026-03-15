from app import create_app

app = create_app()

if __name__ == "__main__":
    # Set debug=False in production to hide tracebacks and use custom error pages
    app.run(debug=False, host="0.0.0.0", port=5000)
