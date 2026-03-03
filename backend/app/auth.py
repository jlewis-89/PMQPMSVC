from fastapi import Depends, HTTPException, Header

def get_current_user(x_user: str = Header(None, alias="X-User")):
    if not x_user:
        raise HTTPException(status_code=401, detail="Unauthorized: missing user header")
    # Minimal in-memory user object; in real life, validate JWT/OAuth token here
    return {"id": x_user, "name": "AutoUser", "roles": ["Editor"]}
