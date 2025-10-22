import json

def lambda_handler(event, context):
    path = event.get("path", "/")
    method = event.get("httpMethod", "GET")
    
    # /hello veya /hello-html
    if path.startswith("/hello"):
        name = "World"
        if method == "GET":
            params = event.get("queryStringParameters") or {}
            name = params.get("name", "World")
        elif method == "POST":
            body = json.loads(event.get("body") or "{}")
            name = body.get("name", "World")
        else:
            return {"statusCode": 405, "body": json.dumps({"error":"Method not allowed"})}
        
        # Eğer HTML endpoint ise
        if path == "/hello-html":
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "text/html"},
                "body": f"""
                <html>
                <head>
                  <style>
                    body {{ font-family: Arial; background: #1e1e1e; color: #00ff00; text-align:center; padding-top:50px;}}
                    h1 {{ font-size: 3em; text-shadow: 2px 2px #000; }}
                  </style>
                </head>
                <body>
                  <h1>Hello, {name}!</h1>
                  <p>Bu fonksiyon bulutta çalışıyor.</p>
                </body>
                </html>
                """
            }
        else:
            return {
                "statusCode": 200,
                "body": json.dumps({"message": f"Hello, {name}!"}),
                "headers": {"Content-Type": "application/json"}
            }
    
    # /square endpoint
    elif path == "/square":
        if method == "POST":
            try:
                payload = event.get("body")
                if isinstance(payload, str):
                    payload = json.loads(payload)
                n = payload.get("n")
                if n is None:
                    raise ValueError("n eksik")
                return {
                    "statusCode": 200,
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps({"n": n, "square": n*n})
                }
            except Exception as e:
                return {
                    "statusCode": 400,
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps({"error": str(e)})
                }
        return {"statusCode": 405, "body": json.dumps({"error":"Method not allowed"})}

    return {"statusCode": 404, "body": json.dumps({"error":"Not found"})}
