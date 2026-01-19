import config_loader

def run_app():
    print("--- Starting Application ---")
  
    if config_loader.is_debug():
        print("[INFO] Debugging is ON")
    
    db = config_loader.get_db()
    print(f"[Connecting] to {db}")
    
   
    key = config_loader.get_key()
    print(f"[Auth] Using Key: {key}")

if __name__ == "__main__":
    run_app()